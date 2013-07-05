#!/usr/bin/env python3
import requests
import json

from statsmile import db


class GetDota:


    def __init__(self, steamid, apikey):
        self.db = db
        self.steamid = steamid
        self.apikey = apikey
        self.dota()


    def dota(self):

        last = []

        options = {'key': self.apikey, 'account_id': self.steamid}
        r = requests.get("https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/", params=options)
        f = json.loads(r.text)

        for mid in f['result']['matches']:
            last.append(mid['match_id'])

        last.sort()
        slices = db.users.find_one({"steamid": self.steamid}, { "matches": { "$slice": 25 } } )

        for key in last:

            if key in slices['matches']:
                pass
            else:
                self.db.users.update({"steamid": self.steamid}, { '$push': {"matches": key}})