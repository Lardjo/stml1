#!/usr/bin/env python3

import logging

from datetime import datetime, timedelta

from motor import Op

from tornado.gen import coroutine
from tornado.escape import json_decode
from tornado.httputil import url_concat
from tornado.httpclient import AsyncHTTPClient


@coroutine
def user_update(db, key, _id, _id32):
    """User update

    Function for getting user profile, update stats and info
    """
    url = url_concat('https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/', {'key': key, 'steamids': _id})

    http_client = AsyncHTTPClient()
    response = yield http_client.fetch(url)

    if response.error:
        logging.warning('User %s has not updated. Error: %s. Code: %s' % (_id, response.error, response.code))
        db.status.update({'key': 'steam_api'}, {'$set': {'value': False, 'time': datetime.now()}})

    else:
        user = json_decode(response.body)['response']['players'][0]
        user = {'persona_name': user['personaname'],
                'profile_url': user['profileurl'],
                'avatar': user['avatarfull'],
                'real_name': user.get('realname', None)}
        db.users.update({'steam_id': _id}, {'$set': user})
        db.status.update({'key': 'steam_api'}, {'$set': {'value': True, 'time': datetime.now()}})
        logging.info('User %s update complete!' % _id)