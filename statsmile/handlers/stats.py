#!/usr/bin/env python3

from motor import Op
from tornado.gen import engine
from tornado.web import asynchronous
from .base import BaseHandler


class StatsHandler(BaseHandler):
    @asynchronous
    @engine
    def get(self):
        session = yield Op(self.db['users'].find_one, {'_id': self.current_user['userid']})
        matches, users = yield [
            Op(self.db['matches'].find().count),
            Op(self.db['users'].find().count)]
        self.render("stats.html", title="Statistics", session=session, users=users, matches=matches)