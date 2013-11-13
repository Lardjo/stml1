#!/usr/bin/env python3

from .base import BaseHandler
from bson import ObjectId


class UserHandler(BaseHandler):
    def get(self, sid=None):
        user = self.application.db["users"].find_one({"_id": ObjectId(sid)})
        matches = self.application.db["matches"].aggregate([
            {"$unwind": "$players"},
            {"$match": {"players.account_id": user["steamid32"]}},
            {"$sort": {"match_id": -1}},
            {"$limit": 10}
        ])
        match = self.application.db["matches"].aggregate([
            {"$match": {"players.account_id": user["steamid32"]}},
            {"$sort": {"match_id": -1}},
            {"$limit": 1}
        ])
        self.render("profile.html", user=user, matches=matches["result"], match=match['result'][0])