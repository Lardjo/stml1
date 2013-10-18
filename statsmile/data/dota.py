#!/usr/bin/env python3
import requests
import json

from .api import apikey
from .mongo import db

def get_dota_matches_id(steamid, **options):

        last = []
        update = []

        options = {'key': apikey, 'account_id': steamid}
        r = requests.get("https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/", params=options)
        f = json.loads(r.text)

        for mid in f['result']['matches']:
            last.append(mid['match_id'])

        last.sort()

        if options.get("update") == "True":

            slices = db.users.find_one({"steamid": steamid}, {"matches": {"$slice": 100}})

            for key in last:

                if key in slices['matches']:
                    pass
                else:
                    update.append(key)

            if not update:
                pass
            else:
                db.users.update({"steamid": steamid}, { '$push': {"matches": {"$each": update}}})

        if options.get("auth") == "True":

            return last