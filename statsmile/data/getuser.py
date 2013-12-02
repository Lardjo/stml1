#!/usr/bin/env python3

import logging

from datetime import datetime, timedelta
from tornado.escape import json_decode
from tornado.httpclient import HTTPClient, HTTPError
from tornado.httputil import url_concat


def converter(steam_id):
    """
    Converter Steam ID 64 to 32
    """
    steam_id_32 = int(steam_id) - 76561197960265728
    return steam_id_32


def get_steam_user(db, steam_id):
    user = None
    key = db["settings"].find_one()
    url = url_concat("http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/",
                     {"key": key["apikey"], "steamids": steam_id})
    http_client = HTTPClient()
    try:
        response = http_client.fetch(url)
        all_user = json_decode(response.body)['response']['players'][0]  # Getting all information
        user = {"steamid": all_user['steamid'],
                "steamid_32": converter(steam_id),
                "personaname": all_user['personaname'],
                "profileurl": all_user['profileurl'],
                "avatar": all_user['avatarfull'],
                "registration": datetime.now(),
                "next_update": datetime.now() + timedelta(minutes=1)}  # Only what need + add update and reg time
        if 'realname' in all_user.keys():  # If user have real name in profile - add him
            user['realname'] = all_user['realname']
        else:
            user['realname'] = None
    except HTTPError as e:
        logging.error("Error: {}".format(e))
    http_client.close()
    logging.info("New user %s has been registered" % user['steamid'])
    return user