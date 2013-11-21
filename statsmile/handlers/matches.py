#!/usr/bin/env python3

from .base import BaseHandler
from bson import ObjectId


class MatchesHandler(BaseHandler):
    def get(self):
        session = self.application.db['users'].find_one({"_id": ObjectId(self.current_user)})
        matches = self.application.db["matches"].find({"game_mode": {"$nin": [7, 9]}}).sort("match_id", -1).limit(20)
        self.render("matches.html", session=session, matches=matches)