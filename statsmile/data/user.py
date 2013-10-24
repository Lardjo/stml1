#!/usr/bin/env python3
import requests

def get_steam_user(db, steamid):
    """
    Get user information
    """
    key = db["settings"].find_one()
    options = {'key': key['apikey'], 'steamids': steamid}
    r = requests.get("http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/", params=options)
    response = r.json()
    return response['response']['players'][0] or {}