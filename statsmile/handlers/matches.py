#!/usr/bin/env python3

from .base import BaseHandler
from bson import ObjectId
from pymongo import DESCENDING


class MatchesHandler(BaseHandler):
    def get(self):
        session = self.application.db['users'].find_one({"_id": ObjectId(self.current_user)})
        matches = list(self.application.db["matches"].find(
            {"game_mode": {"$nin": [7, 9]}}).sort("start_time", DESCENDING).limit(20))
        self.render("matches.html", session=session, matches=matches)