#!/usr/bin/env python3

from tornado.gen import engine
from tornado.web import asynchronous
from .base import BaseHandler
from motor import Op


class MainHandler(BaseHandler):
    @asynchronous
    @engine
    def get(self):
        session = None
        if self.current_user:
            session = yield Op(self.db['users'].find_one, {'_id': self.current_user['userid']})
        self.render('index.html', title="Statsmile", session=session)