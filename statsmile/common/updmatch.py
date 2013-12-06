#!/usr/bin/env python3

import logging

from tornado.gen import coroutine, Wait, Callback
from tornado.escape import json_decode
from tornado.httputil import url_concat
from tornado.httpclient import AsyncHTTPClient
from datetime import datetime


@coroutine
def update_match(db, match_id):
    if match_id is None:
        logging.info("All matches updated! Waiting new matches for getting...")
        return
    key = db["server"].find_one({"key": "apikey"})
    url = url_concat("https://api.steampowered.com/IDOTA2Match_570/GetMatchDetails/V001/",
                     {"match_id": match_id, "key": key["value"]})
    http_client = AsyncHTTPClient()
    http_client.fetch(url, callback=(yield Callback("match_key")))
    response = yield Wait("match_key")
    if response.error:
        logging.warning("Match #%s not updated. Remote server not respond" % match_id)
        db["status"].update({"status": "api_dota"}, {"$set": {"value": "false", "time": datetime.now()}})
    else:
        array = json_decode(response.body)
        db["matches"].insert(array["result"])
        db["status"].update({"status": "api_dota"}, {"$set": {"value": "true", "time": datetime.now()}})
        logging.info("Match #%s added to database" % match_id)