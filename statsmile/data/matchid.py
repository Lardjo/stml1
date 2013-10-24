#!/usr/bin/env python3
import requests
import json

def get_dota_matches_id(db, steamid):

    first = []

    key = db["settings"].find_one()
    options = {'key': key["apikey"], 'account_id': steamid}
    r = requests.get("https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/", params=options)
    f = json.loads(r.text)

    for mid in f['result']['matches']:
        first.append(mid['match_id'])

    first.sort()

    return first