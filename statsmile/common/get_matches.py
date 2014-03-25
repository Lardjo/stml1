#!/usr/bin/env python3

import logging

from datetime import datetime

from motor import Op

from tornado.gen import coroutine, Wait, Callback
from tornado.escape import json_decode
from tornado.httputil import url_concat
from tornado.httpclient import AsyncHTTPClient

from statsmile.parsers import parse_match


@coroutine
def get_matches(db, key, matches):
    """Getting matches

    """

    for match in matches:

        _match = yield Op(db.matches.find_one, {'match_id': match})

        if not _match:

            url = url_concat('https://api.steampowered.com/IDOTA2Match_570/GetMatchDetails/V001/',
                             {'key': key, 'match_id': match})

            http_client = AsyncHTTPClient()
            response = yield http_client.fetch(url)

            if response.error:
                logging.warning('Match with %s id not updated.' % match)
                db.status.update({'key': 'dota_api'}, {'$set': {'value': False, 'time': datetime.now()}})

            else:
                array = json_decode(response.body)['result']

                match = parse_match(array)

                yield Op(db.matches.insert, match)

                logging.debug('MATCH ID: | %s | Success added' % match['match_id'])

        else:
            pass