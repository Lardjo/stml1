#!/usr/bin/env python3

from .base import BaseHandler
from pymongo import DESCENDING
from bson import ObjectId


class UserHandler(BaseHandler):
    def get(self, sid):
        session = self.application.db["users"].find_one({"_id": ObjectId(self.current_user)})
        user = self.application.db["users"].find_one({"_id": ObjectId(sid)})
        matches = list(self.application.db["matches"].find(
            {"players.account_id": user["steamid32"], "game_mode": {"$nin": [7, 9]}},
            {"game_mode": 1, "start_time": 1, "duration": 1, "cluster": 1, "match_id": 1, "radiant_win": 1,
             "players": {"$elemMatch": {"account_id": user["steamid32"]}}}).sort("start_time", DESCENDING).limit(10))
        match = list(self.application.db["matches"].find(
            {"players.account_id": user["steamid32"],
             "game_mode": {"$nin": [7, 9]}}).sort("start_time", DESCENDING).limit(1))
        favorites = self.application.db.matches.aggregate([
            {"$match": {"players.account_id": user["steamid32"], "game_mode": {"$nin": [7, 9]}}},
            {"$project": {"players.hero_id": 1, "players.account_id": 1, "players.count": {"$add": [1]}}},
            {"$unwind": "$players"},
            {"$match": {"players.account_id": user["steamid32"]}},
            {"$group": {"_id": "$players.hero_id", "sum": {"$sum": "$players.count"}}},
            {"$sort": {"sum": -1}},
            {"$limit": 7}
        ])['result']
        self.render("profile.html", user=user, session=session, matches=matches, match=match, favorites=favorites)