#!/usr/bin/env python3

from datetime import datetime, timedelta
from tornado.escape import json_decode
from tornado.httpclient import HTTPClient, HTTPError
from tornado.httputil import url_concat


def get_steam_user(db, log, steamid):

    user = {}

    key = db["settings"].find_one()
    params = {"key": key["apikey"], "steamids": steamid}
    url = url_concat("http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/", params)

    http_client = HTTPClient()

    try:
        response = http_client.fetch(url)
        user = json_decode(response.body)['response']['players'][0]
        user["registration"] = datetime.now()
        user["next_update"] = datetime.now() + timedelta(minutes=1)
    except HTTPError as e:
        log.error("Error: {}".format(e))

    http_client.close()
    return user