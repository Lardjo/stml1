#!/usr/bin/env python3

import tornado.escape

from tornado import gen
from tornado.httputil import url_concat
from tornado.httpclient import AsyncHTTPClient


@gen.coroutine
def getting_matches_id(db, log, steamid):
    matches = []
    start_time = 0
    remaining = 1

    while remaining:
        key = db["settings"].find_one()
        params = {'key': key['apikey'], 'account_id': steamid, 'date_max': start_time}
        url = url_concat("https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/", params)

        response = yield AsyncHTTPClient().fetch(url)

        pack = tornado.escape.json_decode(response.body)

        for match in pack['result']['matches']:

            if not match['match_id'] in matches:
                matches.append(match['match_id'])

        start_time = pack['result']['matches'].pop()['start_time']
        remaining = pack['result']['results_remaining']

    else:
        matches.sort()
        db['users'].update({"steamid": steamid}, {'$set': {"matches": matches}})
        log.info("New user {} successfully added to the database. Added '{}' matches".format(steamid,
                                                                                             len(matches)))