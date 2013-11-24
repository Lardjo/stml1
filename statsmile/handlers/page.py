#!/usr/bin/env python3

from .base import BaseHandler
from bson import ObjectId


class PageHandler(BaseHandler):
    def get(self, source):
        session = self.application.db["users"].find_one({"_id": ObjectId(self.current_user)})
        if source not in ('about', 'privacy', 'start'):
            return self.send_error(404)
        elif source == "about":
            self.render("page.html", title="About", session=session)
        elif source == "privacy":
            self.render("page.html", title="Privacy Policy", session=session)
        elif source == "start":
            self.render("page.html", title="Getting started", session=session)