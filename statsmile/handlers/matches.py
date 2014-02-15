#!/usr/bin/env python3

from motor import Op
from tornado.gen import engine
from tornado.web import asynchronous
from .base import BaseHandler
from statsmile.common import libs


class MatchesHandler(BaseHandler):
    @asynchronous
    @engine
    def get(self):

        session = None
        if self.current_user:
            session = yield Op(self.db['users'].find_one, {'_id': self.current_user['userid']})

        pg = int(self.get_argument('page', 1))

        if pg > 10:
            return self.send_error(404)

        cursor = self.db['matches'].find({'game_mode': {'$nin': [7, 9, 15]}, 'players.hero_id': {'$nin': [0]}},
                                         sort=[("start_time", -1)], limit=20).skip((pg-1)*20)
        matches = yield Op(cursor.to_list)

        self.render('matches.html', title="Statsmile / Matches", page=pg, session=session, matches=matches,
                    cluster=libs.cluster, mode=libs.mode, heroes=libs.heroes)