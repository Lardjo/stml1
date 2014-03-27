#!/usr/bin/env python3

from tornado.gen import coroutine
from tornado.escape import json_decode
from tornado.httputil import url_concat
from tornado.httpclient import AsyncHTTPClient


@coroutine
def get_matches_id(key, steam_id):

    matches = []
    _match_id = 0
    remaining = 1

    while remaining:

        url = url_concat('https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/',
                         {'key': key, 'account_id': steam_id, 'start_at_match_id': _match_id})

        response = yield AsyncHTTPClient().fetch(url)

        if not response.error:

            pack = json_decode(response.body)

            for match in pack['result']['matches']:
                if (not match['match_id'] in matches) and (match['lobby_type'] == 7):
                    matches.append(match['match_id'])

            _match_id = pack['result']['matches'][-1]['match_id']
            remaining = pack['result']['results_remaining']

        else:
            pass

    else:
        matches.sort()

    return matches