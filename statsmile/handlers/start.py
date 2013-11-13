#!/usr/bin/env python3

from .base import BaseHandler


class StartHandler(BaseHandler):
    def get(self):
        settings = self.application.db["settings"].find_one({"apikey": {"$exists": 'true'}})
        if settings:
            self.redirect("/")
            return
        self.render("start.html")

    def post(self):
        settings = {"apikey": self.get_argument("apikey", "")}
        self.application.db["settings"].insert(settings)
        self.redirect("/")
        return
