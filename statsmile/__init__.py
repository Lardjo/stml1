#!/usr/bin/env python3

import os
import logging
import tornado.web

from datetime import datetime, timedelta
from tornado import gen
from tornado.ioloop import IOLoop
from functools import partial
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
        #self.__matches.remove(match)

        new_matches = self.db["users"].aggregate([
            {"$unwind": "$matches"},
            {"$project": {"matches": 1}},
            {"$group": {"_id": "$matches"}},
            {"$match": {"_id": {"$not": {"$in": self.__matches}}}},
            {"$sort": {"_id": -1}}, {"$limit": 1}
        ])

        IOLoop.instance().add_timeout((datetime.now() + timedelta(minutes=2)).timestamp(),
                                      partial(self.periodic_matches, new_matches["result"][0]["_id"]))
        self.__matches.append(new_matches["result"][0]["_id"])

    def __init__(self):
        handlers_list = [
            ("/", handlers.MainHandler),
            ("/auth/login", handlers.AuthHandler),
            ("/auth/logout", handlers.LogoutHandler),
            ("/user/(.*)", handlers.UserHandler),
            ("/about", handlers.AboutHandler),
        ]
        settings = dict(
            cookie_secret="Developed_key",
            gzip=True,
            debug=True,
            login_url="/auth/login",
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static")
        )

        # Database
        try:
            client = MongoClient("localhost", 27017)
            self.db = client["Statsmile"]
        except ConnectionFailure:
            logging.fatal("Database connection can\'t be established, terminating!")
            exit(1)

        # Logger
        if settings["debug"]:
            logging.getLogger().setLevel(logging.DEBUG)
        self.logger = logging.getLogger("high log")

        # Settings
        if not "settings" in self.db.collection_names():
            self.db.create_collection("settings")

        # Matches
        if not "matches" in self.db.collection_names():
            self.db.create_collection("matches")

        # Users updater
        self.__update = []

        users = self.db["users"].find({}).sort("next_update").limit(5)
        for it in users:
            IOLoop.instance().add_timeout(it["next_update"].timestamp(), partial(self.periodic, it))
            self.__update.append(it["_id"])

        # Matches updater
        self.__matches = []

        matches = self.db["users"].aggregate([
            {"$unwind": "$matches"},
            {"$project": {"matches": 1}},
            {"$group": {"_id": "$matches"}},
            {"$sort": {"_id": -1}},
            {"$limit": 5}
        ])
        for mt in matches["result"]:
            IOLoop.instance().add_timeout((datetime.now() + timedelta(minutes=2)).timestamp(),
                                          partial(self.periodic_matches, mt["_id"]))
            self.__matches.append(mt["_id"])

        super().__init__(handlers_list, **settings)

        self.listen(8888)
        self.logger.info("Statsmile server is started!")