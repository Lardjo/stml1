#!/usr/bin/env python3

from .base import BaseHandler


class UserHandler(BaseHandler):
    def get(self, sid=None):
        user = self.application.db["users"].find_one({"steamid": sid})
        self.render("profile.html", user=user)