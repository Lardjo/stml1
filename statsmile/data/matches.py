#!/usr/bin/env python3
import tornado.escape

from tornado import gen
from tornado.httputil import url_concat
from tornado.httpclient import AsyncHTTPClient
from datetime import datetime, timedelta


class GetDota(object):

    def __init__(self, db, log):
        self.db = db
        self.logging = log

    @gen.coroutine
    def get_dota_matches_id(self, steamid):

        last = []
        update = []
        key = self.db["settings"].find_one()
        params = {"key": key["apikey"], "account_id": steamid}
        url = url_concat("https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/", params)

        response = yield AsyncHTTPClient().fetch(url)

        if response.error:
            self.logging.info("User '{}' has not updated. Remote server not respond.".format(steamid))
            return
        else:
            array = tornado.escape.json_decode(response.body)

        for mid in array['result']['matches']:
            last.append(mid['match_id'])

        last.sort()
        slices = self.db['users'].find_one({"steamid": steamid}, {"matches": {"$slice": -100}})

        for key in last:

            if key in slices['matches']:
                pass
            else:
                update.append(key)

        if not update:
            self.logging.info("User '{}' has been updated. New matches not found".format(steamid))
        else:
            self.db['users'].update({"steamid": steamid}, { '$push': {"matches": {"$each": update}}})
            self.logging.info("User '{}' has been updated. Added '{}' matches".format(steamid, len(update)))

        self.db['users'].update({"steamid": steamid}, {'$set': {'next_update': datetime.now() + timedelta(minutes=15)}})