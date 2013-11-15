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
        ])['result']
        match = self.application.db["matches"].aggregate([
            {"$match": {"players.account_id": user["steamid32"]}},
            {"$sort": {"match_id": -1}},
            {"$limit": 1}
        ])['result']
        favorites = self.application.db["matches"].aggregate([
            {"$project": {"players": 1}},
            {"$unwind": "$players"},
            {"$project": {
                "_id": 0,
                "hero": "$players.hero_id",
                "account_id": "$players.account_id",
                "count": {"$add": [1]}
            }},
            {"$match": {"account_id": user["steamid32"]}},
            {"$group": {"_id": "$hero", "sum": {"$sum": "$count"}}},
            {"$sort": {"sum": -1}},
            {"$limit": 10}
        ])['result']
        self.render("profile.html",
                    user=user, matches=matches, match=match, favorites=favorites)