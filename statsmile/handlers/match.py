#!/usr/bin/env python3

from .base import BaseHandler


class MatchHandler(BaseHandler):
    def get(self, match):
        match = self.application.db["matches"].find_one({"match_id": int(match)})
        self.render("match.html", match=match)