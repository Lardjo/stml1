#!/usr/bin/env python3
import requests
import json


class GetDota:

    def __init__(self, steamid, apikey):
        self.steamid = steamid
        self.apikey = apikey
        self.dt2mt = []
        self.dota()

    def dota(self):

        options = {'key': self.apikey, 'account_id': self.steamid}
        r = requests.get("https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/", params=options)
        f = json.loads(r.text)

        for mid in f['result']['matches']:
            self.dt2mt.append(mid['match_id'])

        self.dt2mt.sort()