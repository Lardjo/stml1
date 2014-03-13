#!/usr/bin/env python3

from motor import Op

from tornado.gen import engine
from tornado.web import asynchronous

from .base import BaseHandler
from statsmile.common.json_code import json_encode


class MatchesHandler(BaseHandler):
    def prepare(self):
        super().prepare()
        self.set_header('Content-Type', 'application/json; charset=UTF-8')

    @asynchronous
    @engine
    def get(self):
        matches = {}
        cursor = self.db['matches'].find({'game_mode': {'$nin': [7, 9, 15]}}, sort=[('start_time', -1)], limit=10)
        matches['matches'] = yield Op(cursor.to_list)
        self.write(json_encode(matches))
        self.finish()


class MatchHandler(BaseHandler):
    def prepare(self):
        super().prepare()
        self.set_header('Content-Type', 'application/json; charset=UTF-8')

    @asynchronous
    @engine
    def get(self, match_id):
        match = {}
        response = yield Op(self.db['matches'].find_one, {'match_id': int(match_id)})
        if not response:
            return self.send_error(404)
        match['match'] = response
        self.write(json_encode(match))
        self.finish()