#!/usr/bin/env python3

from datetime import datetime

from tornado.gen import coroutine
from tornado.escape import json_decode
from tornado.httputil import url_concat
from tornado.httpclient import HTTPClient


def get_matches_id():

    key = '35D15682FC2761ED967A0DEBABD499F1'
    _id = '76561198017347096'

    matches = []
    _match_id = 0
    remaining = 1

    print(datetime.now())

    while remaining:

        url = url_concat('https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/',
                         {'key': key, 'account_id': _id, 'start_at_match_id': _match_id})

        response = HTTPClient().fetch(url)

        pack = json_decode(response.body)

        for match in pack['result']['matches']:
            if (not match['match_id'] in matches) and (match['lobby_type'] == 7):
                matches.append(match['match_id'])
        _match_id = pack['result']['matches'][-1]['match_id']
        remaining = pack['result']['results_remaining']
    else:
        matches.sort()
        print(datetime.now())
        print(len(matches))
        return matches

get_matches_id()