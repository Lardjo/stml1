#!/usr/bin/env python3

import logging

from tornado import gen
from tornado.escape import json_decode
from tornado.httputil import url_concat
from tornado.httpclient import AsyncHTTPClient
from datetime import datetime, timedelta


@gen.coroutine
def update_user(db, steamid):
    key = db["server"].find_one({"key": "apikey"})
    url1 = url_concat("https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/",
                      {"key": key["value"], "account_id": steamid})
    url2 = url_concat("http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/",
                      {"key": key["value"], "steamids": steamid})

    http_client = AsyncHTTPClient()

    http_client.fetch(url1, callback=(yield gen.Callback("dota_key")))
    http_client.fetch(url2, callback=(yield gen.Callback("steam_key")))

    response_dota = yield gen.Wait("dota_key")
    response_steam = yield gen.Wait("steam_key")

    if response_dota.error:
        logging.warning("New matches for user %s has not updated. Remote server not respond. "
                        "Code: %s. Error: %s" % (steamid, response_dota.code, response_dota.error))
        db["status"].update({"status": "api_dota"}, {"$set": {"value": "false", "time": datetime.now()}})
    else:
        array = json_decode(response_dota.body)
        new_matches = []
        for_update = []
        for mid in array['result']['matches']:
            new_matches.append(mid['match_id'])
        new_matches.sort()
        slices = db['users'].find_one({"steamid": steamid}, {"matches": {"$slice": -100}})
        for key in new_matches:
            if not key in slices['matches']:
                for_update.append(key)
        db['users'].update({"steamid": steamid}, {'$push': {"matches": {"$each": for_update}}})
        db["status"].update({"status": "api_dota"}, {"$set": {"value": "true", "time": datetime.now()}})
        logging.debug("User %s matches has been updated. Added %s new matches." % (steamid, len(for_update)))

    if response_steam.error:
        logging.warning("User profile %s has not updated. Remote server not respond. "
                        "Code: %s. Error: %s" % (steamid, response_steam.code, response_steam.error))
        db["status"].update({"status": "api_steam"}, {"$set": {"value": "false", "time": datetime.now()}})
    else:
        all_user = json_decode(response_steam.body)['response']['players'][0]
        user = {"steamid": all_user['steamid'],
                "personaname": all_user['personaname'],
                "profileurl": all_user['profileurl'],
                "avatar": all_user['avatarfull']}
        if 'realname' in all_user.keys():
            user["realname"] = all_user["realname"]
        else:
            user["realname"] = None
        db["users"].update({"steamid": steamid}, {"$set": user})
        db["status"].update({"status": "api_steam"}, {"$set": {"value": "true", "time": datetime.now()}})
        logging.debug("User profile %s has been updated." % steamid)

    # Update user count matches
    user = db['users'].find_one({'steamid': steamid})
    matches = db['matches'].find({'players.account_id': user['steamid32'], 'game_mode': {'$nin': [7, 9]}}).count()
    db['users'].update({'steamid': steamid}, {'$set': {"dota_count": matches}})

    db["users"].update({"steamid": steamid}, {"$set": {"update": datetime.now() + timedelta(minutes=5)}})