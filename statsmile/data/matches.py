#!/usr/bin/env python3
import requests
import json

from tornado import gen
from datetime import datetime, timedelta
from statsmile.data import apikey


class GetDota(object):
    def __init__(self, db, log):
        self.db = db
        self.logging = log

    @gen.coroutine
    def get_dota_matches_id(self, steamid):

        last = []
        update = []

        options = {'key': apikey, 'account_id': steamid}
        r = requests.get("https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/", params=options)
        f = json.loads(r.text)

        for mid in f['result']['matches']:
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

        self.db['users'].update(
            {"steamid": steamid},
            {'$set': {
                'next_update': datetime.now() + timedelta(minutes=1)
            }}
        )