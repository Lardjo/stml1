#!/usr/bin/env python3

import logging

from tornado import gen
from tornado.escape import json_decode
from tornado.httputil import url_concat
from tornado.httpclient import AsyncHTTPClient
from datetime import datetime


@gen.coroutine
def update_matches(db, match_id):
    if match_id is None:
        logging.info("All matches updated! Waiting new matches for getting...")
        return
    key = db["settings"].find_one()
    url = url_concat("https://api.steampowered.com/IDOTA2Match_570/GetMatchDetails/V001/",
                     {"match_id": match_id, "key": key["apikey"]})
    http_client = AsyncHTTPClient()
    http_client.fetch(url, callback=(yield gen.Callback("match_key")))
    response = yield gen.Wait("match_key")
    if response.error:
        logging.warning("Match #%s not updated. Remote server not respond" % match_id)
        db["status"].update({"status": "api_dota"}, {"$set": {"value": "false", "time": datetime.now()}})
    else:
        array = json_decode(response.body)
        db["matches"].insert(array["result"])
        db["status"].update({"status": "api_dota"}, {"$set": {"value": "true", "time": datetime.now()}})
        logging.info("Match #%s added to database" % match_id)