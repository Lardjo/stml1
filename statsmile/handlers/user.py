#!/usr/bin/env python3

import math

from .base import BaseHandler
from pymongo import DESCENDING
from bson import ObjectId
from statsmile.common import libs


class UserHandler(BaseHandler):
    def get(self, sid):
        wait = True
        session = self.application.db['sessions'].find_one({'_id': self.current_user})
        if session:
            session = self.application.db['users'].find_one({'_id': session['userid']})
        user = self.application.db['users'].find_one({'_id': ObjectId(sid)})
        if self.application.db["matches"].find_one({"players.account_id": user["steamid32"]}, {"_id": 1}):
            wait = False
        if user is None:
            return self.send_error(404)

        matches = list(self.application.db["matches"].find(
            {"players.account_id": user["steamid32"], "game_mode": {"$nin": [7, 9, 15]}},
            {"game_mode": 1, "start_time": 1, "duration": 1, "cluster": 1,
             "match_id": 1, "radiant_win": 1, "lobby_type": 1,
             "players": {"$elemMatch": {"account_id": user["steamid32"]}}}
        ).sort("start_time", DESCENDING).limit(10))

        match = list(self.application.db["matches"].find(
            {"players.account_id": user["steamid32"],
             "game_mode": {"$nin": [7, 9, 15]}}).sort("start_time", DESCENDING).limit(1))

        favorites = self.application.db.matches.aggregate([
            {"$match": {"players.account_id": user["steamid32"], "game_mode": {"$nin": [7, 9, 15]}}},
            {"$project": {"players.hero_id": 1, "players.account_id": 1, "players.count": {"$add": [1]}}},
            {"$unwind": "$players"},
            {"$match": {"players.account_id": user["steamid32"]}},
            {"$group": {"_id": "$players.hero_id", "sum": {"$sum": "$players.count"}}},
            {"$sort": {"sum": -1}},
            {"$limit": 7}
        ])['result']

        self.render("user.html", title="Dashboard", active="profile", user=user, session=session, matches=matches,
                    match=match, favorites=favorites, wait=wait, heroes=libs.heroes, cluster=libs.cluster,
                    mode=libs.mode)


class UserMatchesHandler(BaseHandler):
    def get(self, sid, page=1):
        pg = int(page)
        user = self.application.db['users'].find_one({'_id': ObjectId(sid)})

        if user is None:
            return self.send_error(404)

        pages = self.application.db["matches"].find({"players.account_id": user['steamid32'],
                                                     "game_mode": {"$nin": [7, 9, 15]}}).count()
        max_pages = math.ceil(pages / 20)

        if pg > max_pages:
            return self.send_error(404)

        if self.application.db["matches"].find_one({"players.account_id": user["steamid32"]}, {"_id": 1}):
            wait = False
        else:
            wait = True

        session = self.application.db['sessions'].find_one({'_id': self.current_user})

        if session:
            session = self.application.db['users'].find_one({'_id': session['userid']})

        matches = list(self.application.db["matches"].find(
            {"players.account_id": user["steamid32"], "game_mode": {"$nin": [7, 9, 15]}},
            {"game_mode": 1, "start_time": 1, "duration": 1, "cluster": 1,
             "match_id": 1, "radiant_win": 1, "lobby_type": 1,
             "players": {"$elemMatch": {"account_id": user["steamid32"]}}}
        ).sort("start_time", DESCENDING).skip((pg-1)*20).limit(20))

        self.render("user.html", title="Matches", active=None, user=user,
                    session=session, wait=wait, matches=matches, max_pages=max_pages, page=pg, heroes=libs.heroes,
                    cluster=libs.cluster, mode=libs.mode)


class UserRecordsHandler(BaseHandler):
    def get(self, sid):
        user = self.application.db['users'].find_one({'_id': ObjectId(sid)})

        if user is None:
            return self.send_error(404)
        session = self.application.db['sessions'].find_one({'_id': self.current_user})

        if session:
            session = self.application.db['users'].find_one({'_id': session['userid']})

        kills = self.application.db["matches"].aggregate([
            {"$match": {"players.account_id": user["steamid32"], "game_mode": {"$nin": [7, 9, 15]}}},
            {"$project": {"match_id": 1, "radiant_win": 1, "start_time": 1, "players.kills": 1,
                          "players.account_id": 1, "players.player_slot": 1, "players.hero_id": 1}},
            {"$unwind": "$players"},
            {"$match": {"players.account_id": user["steamid32"]}},
            {"$sort": {"players.kills": -1}},
            {"$limit": 1}
        ])['result']

        deaths = self.application.db["matches"].aggregate([
            {"$match": {"players.account_id": user["steamid32"], "game_mode": {"$nin": [7, 9, 15]}}},
            {"$project": {"match_id": 1, "radiant_win": 1, "start_time": 1, "players.deaths": 1,
                          "players.account_id": 1, "players.player_slot": 1, "players.hero_id": 1}},
            {"$unwind": "$players"},
            {"$match": {"players.account_id": user["steamid32"]}},
            {"$sort": {"players.deaths": -1}},
            {"$limit": 1}
        ])['result']

        assists = self.application.db["matches"].aggregate([
            {"$match": {"players.account_id": user["steamid32"], "game_mode": {"$nin": [7, 9, 15]}}},
            {"$project": {"match_id": 1, "radiant_win": 1, "start_time": 1, "players.assists": 1,
                          "players.account_id": 1, "players.player_slot": 1, "players.hero_id": 1}},
            {"$unwind": "$players"},
            {"$match": {"players.account_id": user["steamid32"]}},
            {"$sort": {"players.assists": -1}},
            {"$limit": 1}
        ])['result']

        gpm = self.application.db["matches"].aggregate([
            {"$match": {"players.account_id": user["steamid32"], "game_mode": {"$nin": [7, 9, 15]}}},
            {"$project": {"match_id": 1, "radiant_win": 1, "start_time": 1, "players.gold_per_min": 1,
                          "players.account_id": 1, "players.player_slot": 1, "players.hero_id": 1}},
            {"$unwind": "$players"},
            {"$match": {"players.account_id": user["steamid32"]}},
            {"$sort": {"players.gold_per_min": -1}},
            {"$limit": 1}
        ])['result']

        if self.application.db["matches"].find_one({"players.account_id": user["steamid32"]}, {"_id": 1}):
            wait = False
        else:
            wait = True

        self.render("user.html", title="Records", active="records", user=user, session=session,
                    records=(kills, deaths, assists, gpm), wait=wait, heroes=libs.heroes,
                    cluster=libs.cluster, mode=libs.mode)