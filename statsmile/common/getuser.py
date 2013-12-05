#!/usr/bin/env python3

import logging

from tornado.escape import json_decode
from tornado.httpclient import HTTPClient, HTTPError
from tornado.httputil import url_concat

from datetime import datetime


def converter(steamid):
    return int(steamid) - 76561197960265728


def get_steam_user(db, steamid):
    user = None
    key = db['server'].find_one({'key': 'apikey'})
    url = url_concat('http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/',
                     {'key': key['value'], 'steamids': steamid})
    client = HTTPClient()
    try:
        response = client.fetch(url)
        get_user = json_decode(response.body)['response']['players'][0]
        user = {'steamid': get_user['steamid'],
                'steamid32': converter(steamid),
                'personaname': get_user['personaname'],
                'profileurl': get_user['profileurl'],
                'avatar': get_user['avatarfull'],
                'registration': datetime.now(),
                'update': datetime.now()}
        if 'realname' in get_user.keys():
            user['realname'] = get_user['realname']
        else:
            user['realname'] = None
    except HTTPError as e:
        logging.error('Error: %s' % e)
    client.close()
    return user