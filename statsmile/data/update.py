#!/usr/bin/env python3

from tornado import gen
from tornado.escape import json_decode
from tornado.httputil import url_concat
from tornado.httpclient import AsyncHTTPClient
from datetime import datetime, timedelta


@gen.coroutine
def update_matches_id(db, log, steamid):
    last = []
    update = []
    key = db["settings"].find_one()
    params = {"key": key["apikey"], "account_id": steamid}
    params2 = {"key": key["apikey"], "steamids": steamid}
    url = url_concat("https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/", params)
    url2 = url_concat("http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/", params2)

    http_client = AsyncHTTPClient()
    response, response2 = yield [http_client.fetch(url),
                                 http_client.fetch(url2)]
    if response.error or response2.error:
        log.info("User '{}' has not updated. Remote server not respond".format(steamid))
        db['users'].update({"steamid": steamid}, {'$set': {"next_update": datetime.now() + timedelta(minutes=15),
                                                           "last_update": datetime.now()}})
        return
    else:
        array = json_decode(response.body)
        user = json_decode(response2.body)['response']['players'][0]

    for mid in array['result']['matches']:
        last.append(mid['match_id'])

    last.sort()
    slices = db['users'].find_one({"steamid": steamid}, {"matches": {"$slice": -100}})

    for key in last:
        if not key in slices['matches']:
            update.append(key)

    db['users'].update({"steamid": steamid}, {'$set': user})
    db['users'].update({"steamid": steamid}, {'$push': {"matches": {"$each": update}}})
    db['users'].update({"steamid": steamid}, {'$set': {"next_update": datetime.now() + timedelta(minutes=15),
                                                       "last_update": datetime.now()}})
    log.info("User '{}' has been updated. Added '{}' matches".format(steamid, len(update)))