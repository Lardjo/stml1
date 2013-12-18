#!/usr/bin/env python3

from .base import BaseHandler


class StatsHandler(BaseHandler):
    def get(self):
        session = self.application.db['sessions'].find_one({'_id': self.current_user})
        if session:
            session = self.application.db['users'].find_one({'_id': session['userid']})
        matches = self.application.db['matches'].find().count()
        users = self.application.db['users'].find().count()
        self.render("stats.html", title="Statistics", session=session, users=users, matches=matches)