#!/usr/bin/env python3

from bson import ObjectId
from .base import BaseHandler


class UserHandler(BaseHandler):
    def get(self, sid=None):
        session = self.application.db['users'].find_one({"_id": ObjectId(self.current_user)})
        if session:
            self.render("profile.html", session=session)
        else:
            self.render("404.html")