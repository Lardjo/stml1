#!/usr/bin/env python3

import tornado.web

from .base import BaseHandler
from bson import ObjectId


class MatchesHandler(BaseHandler):
    def get(self):
        session = self.application.db['users'].find_one({"_id": ObjectId(self.current_user)})
        matches = self.application.db["matches"].find().sort("match_id", -1).limit(20)
        self.render("matches.html", session=session, matches=matches)

