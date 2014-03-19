#!/usr/bin/env python3

from motor import Op

from tornado.gen import engine
from tornado.web import asynchronous

from .base import BaseHandler


class MainHandler(BaseHandler):
    @asynchronous
    @engine
    def get(self):
        session = None
        if self.current_user:
            session = yield Op(self.db.users.find_one, {'_id': self.current_user['user_id']})
        self.render('index.html', session=session)