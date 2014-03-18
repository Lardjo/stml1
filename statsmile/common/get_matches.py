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
def get_matches(db, match_seq_id):
    """Getting matches

    After getting match id, function sending request to API and getting array matches
    """
    key = yield Op(db.server.find_one, {'key': 'apikey'})

    url = url_concat('https://api.steampowered.com/IDOTA2Match_570/GetMatchHistoryBySequenceNum/V001/',
                     {'key': key['value'], 'start_at_match_seq_num': match_seq_id})

    http_client = AsyncHTTPClient()
    http_client.fetch(url, callback=(yield Callback('match_key')))

    response = yield Wait('match_key')

    if response.error:

        logging.warning('Match array with %s id not updated.' % match_seq_id)
        db.status.update({'key': 'dota_api'}, {'$set': {'value': False, 'time': datetime.now()}})

    else:

        array = json_decode(response.body)['result']

        if array['matches']:

            for match in array['matches']:

                if match['lobby_type'] == 7:  # Only ranked matches

                    match = parse_match(match)

                    _match = yield Op(db['matches'].find_one, {'match_seq_num': match['match_seq_num']})

                    if _match:
                        logging.info('MATCH ID: | %s | MATCH_SEQ_NUM: | %s | Already in database. Pass'
                                     % (match['match_id'], match['match_seq_num']))
                    else:
                        yield Op(db.matches.insert, match)
                        logging.info('MATCH ID: | %s | MATCH_SEQ_NUM: | %s | Success added'
                                     % (match['match_id'], match['match_seq_num']))

                else:
                    pass

            db.server.update({'key': 'last_match_update'},
                             {'$set': {'value': array['matches'][-1]['match_seq_num'] + 1}})

            db.status.update({'key': 'dota_api'}, {'$set': {'value': True, 'time': datetime.now()}})

        else:

            logging.warning('Array of matches is empty')