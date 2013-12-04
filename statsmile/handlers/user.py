#!/usr/bin/env python3

from .base import BaseHandler
from pymongo import DESCENDING
from bson import ObjectId


class UserHandler(BaseHandler):
    def get(self, sid, source):
        session = self.application.db["users"].find_one({"_id": ObjectId(self.current_user)})
        user = self.application.db["users"].find_one({"_id": ObjectId(sid)})

        if user is None:
            return self.send_error(404)
        elif source is None:
            alr = self.application.db["matches"].find_one({"players.account_id": user["steamid_32"]}, {"_id": 1})
            matches = list(self.application.db["matches"].find(
                {"players.account_id": user["steamid_32"], "game_mode": {"$nin": [7, 9]}},
                {"game_mode": 1, "start_time": 1, "duration": 1, "cluster": 1, "match_id": 1, "radiant_win": 1,
                 "players": {"$elemMatch": {"account_id": user["steamid_32"]}}}
            ).sort("start_time", DESCENDING).limit(10))
            match = list(self.application.db["matches"].find(
                {"players.account_id": user["steamid_32"],
                 "game_mode": {"$nin": [7, 9]}}).sort("start_time", DESCENDING).limit(1))
            favorites = self.application.db.matches.aggregate([
                {"$match": {"players.account_id": user["steamid_32"], "game_mode": {"$nin": [7, 9]}}},
                {"$project": {"players.hero_id": 1, "players.account_id": 1, "players.count": {"$add": [1]}}},
                {"$unwind": "$players"},
                {"$match": {"players.account_id": user["steamid_32"]}},
                {"$group": {"_id": "$players.hero_id", "sum": {"$sum": "$players.count"}}},
                {"$sort": {"sum": -1}},
                {"$limit": 7}
            ])['result']
            self.render("user.html", title="Dashboard", user=user, session=session, matches=matches, match=match,
                        favorites=favorites, alr=alr)
        elif source == 'matches':
            alr = self.application.db["matches"].find_one({"players.account_id": user["steamid_32"]}, {"_id": 1})
            matches = list(self.application.db["matches"].find(
                {"players.account_id": user["steamid_32"], "game_mode": {"$nin": [7, 9]}},
                {"game_mode": 1, "start_time": 1, "duration": 1, "cluster": 1, "match_id": 1, "radiant_win": 1,
                 "players": {"$elemMatch": {"account_id": user["steamid_32"]}}}
            ).sort("start_time", DESCENDING).limit(20))
            self.render("user.html", title="Matches", user=user, session=session, matches=matches, alr=alr)
        elif source == 'records':
            alr = self.application.db["matches"].find_one({"players.account_id": user["steamid_32"]}, {"_id": 1})
            kills = self.application.db["matches"].aggregate([
                {"$match": {"players.account_id": user["steamid_32"], "game_mode": {"$nin": [7, 9]}}},
                {"$project": {"match_id": 1, "radiant_win": 1, "start_time": 1, "players.kills": 1,
                              "players.account_id": 1, "players.player_slot": 1, "players.hero_id": 1}},
                {"$unwind": "$players"},
                {"$match": {"players.account_id": user["steamid_32"]}},
                {"$sort": {"players.kills": -1}},
                {"$limit": 1}
            ])['result']
            deaths = self.application.db["matches"].aggregate([
                {"$match": {"players.account_id": user["steamid_32"], "game_mode": {"$nin": [7, 9]}}},
                {"$project": {"match_id": 1, "radiant_win": 1, "start_time": 1, "players.deaths": 1,
                              "players.account_id": 1, "players.player_slot": 1, "players.hero_id": 1}},
                {"$unwind": "$players"},
                {"$match": {"players.account_id": user["steamid_32"]}},
                {"$sort": {"players.deaths": -1}},
                {"$limit": 1}
            ])['result']
            self.render("user.html", title="Records", user=user, session=session, records=(kills, deaths), alr=alr)
        else:
            return self.send_error(404)