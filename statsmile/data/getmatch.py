#!/usr/bin/env python3

from tornado import gen
from tornado.escape import json_decode
from tornado.httputil import url_concat
from tornado.httpclient import AsyncHTTPClient


@gen.coroutine
def update_matches(db, log, match_id):
    if match_id is None:
        log.info("All matches updated! Waiting new matches for getting")
        return
    key = db["settings"].find_one()
    params = {"match_id": match_id, "key": key["apikey"]}
    url = url_concat("https://api.steampowered.com/IDOTA2Match_570/GetMatchDetails/V001/", params)

    response = yield AsyncHTTPClient().fetch(url)
    if response.error:
        log.info("Match #'{}' not updated. Remote server not respond".format(match_id))
        return
    else:
        array = json_decode(response.body)

    db["matches"].insert(array["result"])
    log.info("Match #'{}' added to database".format(match_id))
