#!/usr/bin/env python3

from motor import Op

from tornado.gen import engine
from tornado.web import asynchronous

from statsmile.common.json_code import json_encode
from .base import BaseHandler


class MatchesHandler(BaseHandler):

    def prepare(self):
        super().prepare()
        self.set_header('Content-Type', 'application/json; charset=UTF-8')

    @asynchronous
    @engine
    def get(self):
        array = dict()

        mode = self.get_argument('game_mode', 1)

        if mode not in (1, 2, 16):
            mode = 1

        account_id = self.get_argument('account_id', None)

        if account_id:

            cursor = self.db.matches.find({'players.account_id': int(account_id),
                                           'game_mode': int(mode),
                                           'unregistered': {'$exists': False}}, sort=[('start_time', -1)], limit=10)
        else:

            cursor = self.db.matches.find({'game_mode': int(mode), 'unregistered': {'$exists': False}},
                                          sort=[('start_time', -1)], limit=20)

        array['matches'] = yield Op(cursor.to_list)
        self.write(json_encode(array))
        self.finish()


class MatchHandler(BaseHandler):

    def prepare(self):
        super().prepare()
        self.set_header('Content-Type', 'application/json; charset=UTF-8')

    @asynchronous
    @engine
    def get(self, match_id):
        array = dict()
        array['match'] = yield Op(self.db.matches.find_one, {'match_id': int(match_id)})
        self.write(json_encode(array))
        self.finish()