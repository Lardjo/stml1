#!/usr/bin/env python3

from motor import Op
from tornado.gen import engine
from tornado.web import asynchronous
from .base import BaseHandler


class PlayersHandler(BaseHandler):
    @asynchronous
    @engine
    def get(self):
        cursor = self.application.db['users'].find(sort=[('dota_count', -1)], limit=20)
        players = yield Op(cursor.to_list)
        session = yield Op(self.db['users'].find_one, {'_id': self.current_user['userid']})
        self.render('players.html', title='Statsmile / Players', session=session, players=players)