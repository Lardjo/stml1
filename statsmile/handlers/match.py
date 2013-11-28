#!/usr/bin/env python3

from bson import ObjectId

from .base import BaseHandler


class MatchHandler(BaseHandler):
    def get(self, match):
        session = self.application.db["users"].find_one({"_id": ObjectId(self.current_user)})
        match = self.application.db["matches"].find_one({"match_id": int(match)})
        if match is None:
            return self.send_error(404)
        self.render("match.html", session=session, match=match)