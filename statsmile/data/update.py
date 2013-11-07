#!/usr/bin/env python3

import tornado.escape

from tornado import gen
from tornado.httputil import url_concat
from tornado.httpclient import AsyncHTTPClient
from datetime import datetime, timedelta


@gen.coroutine
def update_matches_id(db, log, steamid):
    last = []
    update = []
    key = db["settings"].find_one()
    params = {"key": key["apikey"], "account_id": steamid}
    url = url_concat("https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/", params)

    response = yield AsyncHTTPClient().fetch(url)
    if response.error:
        log.info("User '{}' has not updated. Remote server not respond".format(steamid))
        db['users'].update({"steamid": steamid}, {'$set': {"next_update": datetime.now() + timedelta(minutes=15),
                                                           "last_update": datetime.now()}})
        return
    else:
        array = tornado.escape.json_decode(response.body)

    for mid in array['result']['matches']:
        last.append(mid['match_id'])

    last.sort()
    slices = db['users'].find_one({"steamid": steamid}, {"matches": {"$slice": -100}})

    for key in last:
        if key in slices['matches']:
            pass
        else:
            update.append(key)

    if not update:
        log.info("User '{}' has been updated. New matches not found".format(steamid))
    else:
        db['users'].update({"steamid": steamid}, {'$push': {"matches": {"$each": update}}})
        log.info("User '{}' has been updated. Added '{}' matches".format(steamid, len(update)))

    db['users'].update({"steamid": steamid}, {'$set': {"next_update": datetime.now() + timedelta(minutes=15),
                                                       "last_update": datetime.now()}})


@gen.coroutine
def update_matches(db, log, match_id):
    key = db["settings"].find_one()
    params = {"match_id": match_id, "key": key["apikey"]}
    url = url_concat("https://api.steampowered.com/IDOTA2Match_570/GetMatchDetails/V001/", params)

    response = yield AsyncHTTPClient().fetch(url)
    if response.error:
        log.info("Match #'{}' not updated. Remote server not respond".format(match_id))
        return
    else:
        array = tornado.escape.json_decode(response.body)

    db["matches"].insert({"match_id": match_id, "result": array["result"]})
    log.info("Match #'{}' added to database".format(match_id))
