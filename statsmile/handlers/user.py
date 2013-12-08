#!/usr/bin/env python3

from .base import BaseHandler
from pymongo import DESCENDING
from bson import ObjectId


class UserHandler(BaseHandler):
    def get(self, sid, source):
        wait = True
        session = self.application.db['sessions'].find_one({'_id': self.current_user})
        if session:
            session = self.application.db['users'].find_one({'_id': session['userid']})
        user = self.application.db['users'].find_one({'_id': ObjectId(sid)})
        if self.application.db["matches"].find_one({"players.account_id": user["steamid32"]}, {"_id": 1}):
            wait = False
        if user is None:
            return self.send_error(404)
        elif source is None:
            matches = list(self.application.db["matches"].find(
                {"players.account_id": user["steamid32"], "game_mode": {"$nin": [7, 9]}},
                {"game_mode": 1, "start_time": 1, "duration": 1, "cluster": 1, "match_id": 1, "radiant_win": 1,
                 "players": {"$elemMatch": {"account_id": user["steamid32"]}}}
            ).sort("start_time", DESCENDING).limit(10))
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
            self.render("user.html", title="Dashboard", active="profile", user=user, session=session, matches=matches,
                        match=match, favorites=favorites, wait=wait)
        elif source == 'matches':
            matches = list(self.application.db["matches"].find(
                {"players.account_id": user["steamid32"], "game_mode": {"$nin": [7, 9]}},
                {"game_mode": 1, "start_time": 1, "duration": 1, "cluster": 1, "match_id": 1, "radiant_win": 1,
                 "players": {"$elemMatch": {"account_id": user["steamid32"]}}}
            ).sort("start_time", DESCENDING).limit(20))
            self.render("user.html", title="Matches", active="profile", user=user, session=session, matches=matches,
                        wait=wait)
        elif source == 'records':
            kills = self.application.db["matches"].aggregate([
                {"$match": {"players.account_id": user["steamid32"], "game_mode": {"$nin": [7, 9]}}},
                {"$project": {"match_id": 1, "radiant_win": 1, "start_time": 1, "players.kills": 1,
                              "players.account_id": 1, "players.player_slot": 1, "players.hero_id": 1}},
                {"$unwind": "$players"},
                {"$match": {"players.account_id": user["steamid32"]}},
                {"$sort": {"players.kills": -1}},
                {"$limit": 1}
            ])['result']
            deaths = self.application.db["matches"].aggregate([
                {"$match": {"players.account_id": user["steamid32"], "game_mode": {"$nin": [7, 9]}}},
                {"$project": {"match_id": 1, "radiant_win": 1, "start_time": 1, "players.deaths": 1,
                              "players.account_id": 1, "players.player_slot": 1, "players.hero_id": 1}},
                {"$unwind": "$players"},
                {"$match": {"players.account_id": user["steamid32"]}},
                {"$sort": {"players.deaths": -1}},
                {"$limit": 1}
            ])['result']
            assists = self.application.db["matches"].aggregate([
                {"$match": {"players.account_id": user["steamid32"], "game_mode": {"$nin": [7, 9]}}},
                {"$project": {"match_id": 1, "radiant_win": 1, "start_time": 1, "players.assists": 1,
                              "players.account_id": 1, "players.player_slot": 1, "players.hero_id": 1}},
                {"$unwind": "$players"},
                {"$match": {"players.account_id": user["steamid32"]}},
                {"$sort": {"players.assists": -1}},
                {"$limit": 1}
            ])['result']
            gpm = self.application.db["matches"].aggregate([
                {"$match": {"players.account_id": user["steamid32"], "game_mode": {"$nin": [7, 9]}}},
                {"$project": {"match_id": 1, "radiant_win": 1, "start_time": 1, "players.gold_per_min": 1,
                              "players.account_id": 1, "players.player_slot": 1, "players.hero_id": 1}},
                {"$unwind": "$players"},
                {"$match": {"players.account_id": user["steamid32"]}},
                {"$sort": {"players.gold_per_min": -1}},
                {"$limit": 1}
            ])['result']
            self.render("user.html", title="Records", active="records", user=user, session=session,
                        records=(kills, deaths, assists, gpm), wait=wait)
        else:
            return self.send_error(404)