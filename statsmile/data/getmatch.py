#!/usr/bin/env python3

import tornado.escape

from tornado import gen
from tornado.httputil import url_concat
from tornado.httpclient import AsyncHTTPClient


@gen.coroutine
def update_matches(db, log, match_id):
    key = db["settings"].find_one()
    params = {"match_id": match_id, "key": key["apikey"]}
    url = url_concat("https://api.steampowered.com/IDOTA2Match_570/GetMatchDetails/V001/", params)

    response = yield AsyncHTTPClient().fetch(url)
    if response.error:
        log.info("Match #'{}' not updated. Remote server not respond".format(match_id))
        return
    else:
        array = tornado.escape.json_decode(response.body)

    db["matches"].insert({"match_id": match_id, "result": array["result"]})
    log.info("Match #'{}' added to database".format(match_id))
