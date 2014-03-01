#!/usr/bin/env python3

from motor import Op

from tornado.gen import engine
from tornado.web import asynchronous
from tornado.escape import json_decode, json_encode
from tornado.httputil import url_concat
from tornado.httpclient import AsyncHTTPClient

from .base import BaseHandler


class MatchesHandler(BaseHandler):
    def prepare(self):
        super().prepare()
        self.set_header('Content-Type', 'application/json; charset=UTF-8')

    @asynchronous
    @engine
    def get(self):
        print('hui')
        key = yield Op(self.db['server'].find_one, {'key': 'apikey'})
        params = {'key': key['value']}
        url = url_concat('http://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/', params)
        response = yield AsyncHTTPClient().fetch(url)
        pack = json_decode(response.body)
        self.write(json_encode(pack['result']['matches'][:5]))
        self.finish()