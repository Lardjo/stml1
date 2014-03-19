#!/usr/bin/env python3

import logging

from tornado.gen import coroutine
from tornado.escape import json_decode
from tornado.httpclient import HTTPClient, HTTPError
from tornado.httputil import url_concat

from datetime import datetime, timedelta


def converter(steamid):
    return int(steamid) - 76561197960265728


@coroutine
def get_user(key, steamid):
    user = None
    url = url_concat('https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/', {'key': key,
                                                                                           'steamids': steamid})
    client = HTTPClient()

    try:
        response = client.fetch(url)
        array = json_decode(response.body)['response']['players'][0]
        user = {'steam_id': array['steamid'],
                'steam_id32': converter(steamid),
                'persona_name': array['personaname'],
                'profile_url': array['profileurl'],
                'avatar': array['avatarfull'],
                'registration': datetime.now(),
                'updated': datetime.now() + timedelta(minutes=1)}

        if 'realname' in array.keys():
            user['real_name'] = array['realname']
        else:
            user['real_name'] = None

    except HTTPError as e:
        logging.error('Error: %s' % e)

    client.close()
    return user