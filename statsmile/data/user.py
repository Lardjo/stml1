#!/usr/bin/env python3
import tornado.escape

from tornado import httpclient
from tornado.httputil import url_concat


def get_steam_user(db, log, steamid):

    array = None

    key = db["settings"].find_one()
    params = {'key': key['apikey'], 'steamids': steamid}
    url = url_concat("http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/", params)

    http_client = httpclient.HTTPClient()

    try:
        response = http_client.fetch(url)
        array = tornado.escape.json_decode(response.body)
    except httpclient.HTTPError as e:
        log.info("HTTP Error:", e)

    http_client.close()

    return array['response']['players'][0] or {}