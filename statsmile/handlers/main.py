#!/usr/bin/env python3

from .base import BaseHandler


class MainHandler(BaseHandler):
    def get(self):
        session = self.application.db['sessions'].find_one({'_id': self.current_user})
        user = self.application.db['users'].find_one({'_id': session['userid']})
        self.render("index.html", title="Statsmile", user=user)