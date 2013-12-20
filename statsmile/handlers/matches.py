#!/usr/bin/env python3

from motor import Op
from tornado.gen import engine
from tornado.web import asynchronous
from .base import BaseHandler
from statsmile.common import libs


class MatchesHandler(BaseHandler):
    @asynchronous
    @engine
    def get(self, page=1):
        pg = int(page)
        if pg > 10:
            return self.send_error(404)
        cursor = self.application.db["matches"].find(
            {"game_mode": {"$nin": [7, 9, 15]}}, sort=[("start_time", -1)], limit=20).skip((pg-1)*20)
        matches = yield Op(cursor.to_list)
        session = yield Op(self.db['users'].find_one, {'_id': self.current_user['userid']})
        self.render('matches.html', title="Statsmile / Matches", page=pg, session=session, matches=matches,
                    cluster=libs.cluster, mode=libs.mode, heroes=libs.heroes)