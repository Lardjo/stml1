#!/usr/bin/env python3

from .base import BaseHandler
from pymongo import DESCENDING


class MatchesHandler(BaseHandler):
    def get(self, page=1):
        pg = int(page)
        if pg > 10:
            self.send_error(404)
        matches = list(self.application.db["matches"].find({
            "game_mode": {"$nin": [7, 9]}}).sort("start_time", DESCENDING).skip((pg-1)*20).limit(20))
        session = self.application.db['sessions'].find_one({'_id': self.current_user})
        if session:
            session = self.application.db['users'].find_one({'_id': session['userid']})
        self.render('matches.html', title="Statsmile / Matches", active="matches", page=pg,
                    session=session, matches=matches)
