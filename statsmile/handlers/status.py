#!/usr/bin/env python3

from motor import Op
from tornado.gen import engine
from tornado.web import asynchronous
from .base import BaseHandler


class StatusHandler(BaseHandler):
    @asynchronous
    @engine
    def get(self):
        session = None
        if self.current_user:
            session = yield Op(self.db['users'].find_one, {'_id': self.current_user['userid']})
        st_dota, st_steam = yield [
            Op(self.db['status'].find_one, {'status': 'api_dota'}),
            Op(self.db['status'].find_one, {'status': 'api_steam'})]
        self.render("status.html", title="Status", session=session, dota=st_dota, steam=st_steam)