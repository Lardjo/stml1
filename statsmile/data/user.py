#!/usr/bin/env python3
import tornado.escape
import requests

from tornado import httpclient
from tornado.httputil import url_concat


def get_steam_user(db, log, steamid):

    key = db["settings"].find_one()
    params = {'key': key['apikey'], 'steamids': steamid}
    r = requests.get("http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/", params=params)
    response = r.json()

    return response['response']['players'][0] or {}