#!/usr/bin/env python3

from motor import Op
from tornado.gen import engine
from tornado.web import asynchronous
from .base import BaseHandler


class PagesHandler(BaseHandler):
    @asynchronous
    @engine
    def get(self, source):
        session = None
        if self.current_user:
            session = yield Op(self.db['users'].find_one, {'_id': self.current_user['userid']})
        if source not in ('about', 'privacy', 'faq', 'status', 'license'):
            return self.send_error(404)
        elif source == "about":
            self.render("pages.html", title="About", session=session)
        elif source == "privacy":
            self.render("pages.html", title="Privacy Policy", session=session)
        elif source == "faq":
            self.render("pages.html", title="FAQ", session=session)
        elif source == "license":
            self.render("pages.html", title="License", session=session)