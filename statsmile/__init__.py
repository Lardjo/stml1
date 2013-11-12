#!/usr/bin/env python3

import os
import logging
import tornado.web

from datetime import datetime, timedelta
from functools import partial
from tornado import gen
from tornado.ioloop import IOLoop
from pymongo import MongoClient, ASCENDING
from pymongo.errors import ConnectionFailure
from statsmile import handlers
from statsmile.data import update_matches_id, update_matches


class Statsmile(tornado.web.Application):
    @gen.coroutine
    def periodic(self, user):
        self.logger.debug("Started updating '{}' user".format(user["steamid"]))

        yield update_matches_id(self.db, self.logger, user["steamid"])
        self.__update.remove(user["_id"])

        new_match = self.db["users"].find_one({"_id": {"$not": {"$in": self.__update}}},
                                              sort=[("next_update", ASCENDING)], limit=1)

        IOLoop.instance().add_timeout(new_match["next_update"].timestamp(), partial(self.periodic, new_match))
        self.__update.append(new_match["_id"])

    @gen.coroutine
    def periodic_matches(self, match):
        self.logger.info("Start receiving data match '{}'...".format(match))

        yield update_matches(self.db, self.logger, match)

        complete = self.db["matches"].aggregate({"$group": {"_id": "matches", "items": {"$addToSet": "$match_id"}}})

        new_matches = self.db["users"].aggregate([
            {"$unwind": "$matches"},
            {"$project": {"matches": 1}},
            {"$group": {"_id": "$matches"}},
            {"$match": {"_id": {"$not": {"$in": complete["result"][0]["items"]}}}},
            {"$sort": {"_id": -1}},
            {"$limit": 1}
        ])

        IOLoop.instance().add_timeout((datetime.now() + timedelta(minutes=1)).timestamp(),
                                      partial(self.periodic_matches, new_matches["result"][0]["_id"]))

    def init_db(self):
        try:
            client = MongoClient("localhost", 27017)
            return client["Statsmile"]
        except ConnectionFailure:
            logging.fatal("Database connection can\'t be established, terminating!")
            exit(1)

    def __init__(self):
        handlers_list = [
            ("/", handlers.MainHandler),
            ("/start", handlers.StartHandler),
            ("/auth/login", handlers.AuthHandler),
            ("/auth/logout", handlers.LogoutHandler),
            ("/user/(.*)", handlers.UserHandler),
            ("/matches", handlers.MatchesHandler),
            ("/players", handlers.PlayersHandler),
            ("/about", handlers.AboutHandler),
        ]
        settings = {
            "cookie_secret": "Developed_key",
            "gzip": True,
            "debug": True,
            "template_path": os.path.join(os.path.dirname(__file__), "templates"),
            "static_path": os.path.join(os.path.dirname(__file__), "static"),
            "login_url": "/auth/login"
        }

        # Database
        self.db = self.init_db()

        # Logger
        if settings["debug"]:
            logging.getLogger().setLevel(logging.DEBUG)
        self.logger = logging.getLogger("high log")

        # Settings and Matches
        if not "settings" in self.db.collection_names():
            self.db.create_collection("settings")

        if not "matches" in self.db.collection_names():
            self.db.create_collection("matches")

        # Users updater
        self.__update = []

        users = self.db["users"].find({}).sort("next_update").limit(5)
        for it in users:
            IOLoop.instance().add_timeout(it["next_update"].timestamp(), partial(self.periodic, it))
            self.__update.append(it["_id"])

        # Matches updater
        complete = self.db["matches"].aggregate({"$group": {"_id": "matches", "items": {"$addToSet": "$match_id"}}})
        if not complete["result"]:
            matches = self.db["users"].aggregate([
                {"$unwind": "$matches"},
                {"$project": {"matches": 1}},
                {"$group": {"_id": "$matches"}},
                {"$sort": {"_id": -1}},
                {"$limit": 1}
            ])
        else:
            matches = self.db["users"].aggregate([
                {"$unwind": "$matches"},
                {"$project": {"matches": 1}},
                {"$group": {"_id": "$matches"}},
                {"$match": {"_id": {"$not": {"$in": complete["result"][0]["items"]}}}},
                {"$sort": {"_id": -1}},
                {"$limit": 1}
            ])
        for mt in matches["result"]:
            IOLoop.instance().add_timeout((datetime.now() + timedelta(minutes=1)).timestamp(),
                                          partial(self.periodic_matches, mt["_id"]))

        super().__init__(handlers_list, **settings)

        self.listen(8888)
        self.logger.info("Statsmile server is started!")