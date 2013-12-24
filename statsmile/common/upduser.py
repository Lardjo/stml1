#!/usr/bin/env python3

import logging

from motor import Op
from tornado.gen import coroutine, Task
from tornado.escape import json_decode
from tornado.httputil import url_concat
from tornado.httpclient import AsyncHTTPClient
from datetime import datetime, timedelta


@coroutine
def update_user(db, steamid):

    # TODO: Black List need move to the server configuration
    black_list = [7, 9, 15]

    key = yield Op(db["server"].find_one, {"key": "apikey"})

    url1 = url_concat("http://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/",
                      {"key": key["value"], "account_id": steamid})
    url2 = url_concat("http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/",
                      {"key": key["value"], "steamids": steamid})

    http_client = AsyncHTTPClient()

    response_dota, response_steam = yield [Task(http_client.fetch, url1),
                                           Task(http_client.fetch, url2)]

    if response_dota.error:
        logging.warning("New matches for user %s has not updated. Error: %s" % (steamid, response_dota.error))
        db["status"].update({"status": "api_dota"}, {"$set": {"value": "false", "time": datetime.now()}})
    else:
        array = json_decode(response_dota.body)
        new_matches = []
        for_update = []
        for mid in array['result']['matches']:
            new_matches.append(mid['match_id'])
        new_matches.sort()
        slices = yield Op(db['users'].find_one, {"steamid": steamid}, {"matches": {"$slice": -100}})
        for key in new_matches:
            if not key in slices['matches']:
                for_update.append(key)
        db['users'].update({"steamid": steamid}, {'$push': {"matches": {"$each": for_update}}})
        db["status"].update({"status": "api_dota"}, {"$set": {"value": "true", "time": datetime.now()}})
        logging.info('User matches %s has been updated. Added %s matches' % (steamid, len(for_update)))

    if response_steam.error:
        logging.warning("User profile %s has not updated. Error: %s" % (steamid, response_steam.error))
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
        logging.info('User profile %s has been updated' % steamid)

    # Update user count matches
    user = yield Op(db['users'].find_one, {'steamid': steamid})

    matches = yield Op(db['matches'].find({'players.account_id': user['steamid32'],
                                           'game_mode': {'$nin': black_list}}).count)

    db['users'].update({'steamid': steamid}, {'$set': {'dota_count': matches,
                                                       'update': datetime.now() + timedelta(minutes=5),
                                                       'last_update': datetime.now()}})