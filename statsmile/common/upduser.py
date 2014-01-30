#!/usr/bin/env python3

import logging
import time

from motor import Op
from tornado.gen import coroutine, Task
from tornado.escape import json_decode
from tornado.httputil import url_concat
from tornado.httpclient import AsyncHTTPClient
from datetime import datetime, timedelta


@coroutine
def update_user(db, steamid):

    # TODO: Black List should move to the server configuration
    black_list = [7, 9, 15]

    key = yield Op(db["server"].find_one, {"key": "apikey"})

    http_client = AsyncHTTPClient()

    dota, steam = yield [Task(http_client.fetch,
                              url_concat("https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/",
                                         {"key": key["value"], "account_id": steamid})),
                         Task(http_client.fetch,
                              url_concat("https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/",
                                         {"key": key["value"], "steamids": steamid}))]

    if dota.error or dota.code != 200:
        logging.warning("New matches for %s has not updated. Error: %s. Code: %s" % (steamid, dota.error, dota.code))
        db['status'].update({"status": "api_dota"}, {"$set": {"value": "false", "time": datetime.now()}}, w=1)
    else:
        array = json_decode(dota.body)
        if array['result']['status'] == 15:
            logging.info('User %s not allow getting his matches. Private profile. Pass' % steamid)
        else:
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
            db['status'].update({"status": "api_dota"}, {"$set": {"value": "true", "time": datetime.now()}}, w=1)

    if steam.error or steam.code != 200:
        logging.warning("User profile %s has not updated. Error: %s. Code: %s" % (steamid, steam.error, steam.code))
        db['status'].update({"status": "api_steam"}, {"$set": {"value": "false", "time": datetime.now()}}, w=1)
    else:
        player = json_decode(steam.body)['response']['players'][0]
        user = {'steamid': player['steamid'],
                'personaname': player['personaname'],
                'profileurl': player['profileurl'],
                'avatar': player['avatarfull'],
                'realname': player.get('realname', None)}
        db["users"].update({"steamid": steamid}, {"$set": user})
        db["status"].update({"status": "api_steam"}, {"$set": {"value": "true", "time": datetime.now()}}, w=1)

    user = yield Op(db['users'].find_one, {'steamid': steamid})

    # Update user count matches
    matches = yield Op(db['matches'].find({'players.account_id': user['steamid32'],
                                           'game_mode': {'$nin': black_list},
                                           'players.hero_id': {'$nin': [0]}}).count)

    # Update user favorites
    favorites = yield Op(db['matches'].aggregate,
                         [{"$match": {'players.account_id': user["steamid32"],
                                      'game_mode': {"$nin": black_list},
                                      'players.hero_id': {'$nin': [0]}}},
                          {"$project": {"players.hero_id": 1, "players.account_id": 1, "players.count": {"$add": [1]}}},
                          {"$unwind": "$players"},
                          {"$match": {"players.account_id": user["steamid32"]}},
                          {"$group": {"_id": "$players.hero_id", "sum": {"$sum": "$players.count"}}},
                          {"$sort": {"sum": -1}},
                          {"$limit": 115}])

    # Update user total hours
    pub, events = yield [
        Op(db['matches'].aggregate,
           [{"$match": {"players.account_id": user["steamid32"], "game_mode": {"$nin": black_list}}},
            {"$group": {"_id": 'None', "sum": {"$sum": "$duration"}}}]),
        Op(db['matches'].aggregate,
           [{"$match": {"players.account_id": user["steamid32"], "game_mode": {"$in": black_list}}},
            {"$group": {"_id": 'None', "sum": {"$sum": "$duration"}}}])]

    # Update recent game activity
    matchesPlayed2Wk = yield Op(db['matches'].find({'start_time': {'$lt': time.time(),
                                                                   '$gte': time.time()-1209600},
                                                    'players.account_id': user['steamid32'],
                                                    'game_mode': {'$nin': black_list},
                                                    'players.hero_id': {'$nin': [0]}}).count)

    db['users'].update({'steamid': steamid},
                       {'$set': {
                           'dota_count': matches,
                           'matchesPlayed2Wk': matchesPlayed2Wk,
                           'favorites': favorites['result'],
                           'total_hours': {'public': pub['result'][0]['sum'] if len(pub['result']) > 0 else 0,
                                           'events': events['result'][0]['sum'] if len(events['result']) > 0 else 0}}})

    logging.info('User %s update complete!' % steamid)