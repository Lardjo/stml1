#!/usr/bin/env python3
import requests
import json

from .api import apikey

def get_dota_matches_id(steamid):

    first = []

    options = {'key': apikey, 'account_id': steamid}
    r = requests.get("https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/", params=options)
    f = json.loads(r.text)

    for mid in f['result']['matches']:
        first.append(mid['match_id'])

    first.sort()

    return first