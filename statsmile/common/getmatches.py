#!/usr/bin/env python3

import logging

from motor import Op
from tornado.gen import coroutine
from tornado.escape import json_decode
from tornado.httputil import url_concat
from tornado.httpclient import AsyncHTTPClient


@coroutine
def getting_matches(db, steamid):
    logging.debug('Getting all matches for user %s...' % steamid)

    matches = []
    start_time = 0
    remaining = 1

    while remaining:
        key = yield Op(db['server'].find_one, {'key': 'apikey'})
        params = {'key': key['value'], 'account_id': steamid, 'date_max': start_time}
        url = url_concat('http://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/', params)
        response = yield AsyncHTTPClient().fetch(url)
        pack = json_decode(response.body)
        for match in pack['result']['matches']:
            if not match['match_id'] in matches:
                matches.append(match['match_id'])
        start_time = pack['result']['matches'].pop()['start_time']
        remaining = pack['result']['results_remaining']
    else:
        matches.sort()
        db['users'].update({'steamid': steamid}, {'$set': {'matches': matches}})
        logging.info('User %s successfully added to the database. Added %s matches' % (steamid, len(matches)))