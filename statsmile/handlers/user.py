#!/usr/bin/env python3

from bson import ObjectId
from .base import BaseHandler


class UserHandler(BaseHandler):
    def get(self, sid=None):
        last = []
        session = self.application.db['users'].find_one({"_id": ObjectId(self.current_user)})
        for it in reversed(session["matches"][-5:]):
            match = self.application.db["matches"].find_one({"match_id": it})
            last.append(match)
        if session:
            self.render("profile.html", session=session, matches=last)
        else:
            self.render("404.html")