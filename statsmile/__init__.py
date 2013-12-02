import os
import logging
import tornado.web


from datetime import datetime, timedelta
from random import choice
from string import ascii_letters, digits
from functools import partial
from tornado import gen
from tornado.ioloop import IOLoop
from pymongo import MongoClient, ASCENDING, DESCENDING
from pymongo.errors import ConnectionFailure, DuplicateKeyError
from statsmile import handlers
from statsmile.data import update_matches_id, update_matches


class Statsmile(tornado.web.Application):
    @gen.coroutine
    def periodic(self, user):
        self.logger.debug("Started updating %s user" % user["steamid"])

        yield update_matches_id(self.db, user["steamid"])
        self.__update.remove(user["_id"])

        new_match = self.db["users"].find_one({"_id": {"$not": {"$in": self.__update}}},
                                              sort=[("next_update", ASCENDING)], limit=1)

        IOLoop.instance().add_timeout(new_match["next_update"].timestamp(), partial(self.periodic, new_match))
        self.__update.append(new_match["_id"])

    @gen.coroutine
    def periodic_matches(self, match):
        self.logger.info("Start receiving data match %s" % match)

        yield update_matches(self.db, match)

        complete = self.db["matches"].aggregate({"$group": {"_id": "matches", "items": {"$addToSet": "$match_id"}}})

        new_matches = self.db["users"].aggregate([
            {"$unwind": "$matches"},
            {"$project": {"matches": 1}},
            {"$group": {"_id": "$matches"}},
            {"$match": {"_id": {"$not": {"$in": complete["result"][0]["items"]}}}},
            {"$sort": {"_id": -1}},
            {"$limit": 1}
        ])

        if not new_matches['result']:
            IOLoop.instance().add_timeout((datetime.now() + timedelta(minutes=5)).timestamp(),
                                          partial(self.periodic_matches, None))
        else:
            IOLoop.instance().add_timeout((datetime.now() + timedelta(seconds=10)).timestamp(),
                                          partial(self.periodic_matches, new_matches['result'][0]['_id']))

    def get_cookies(self, key):
        _ = self.db['settings'].find_one({'key': key}, fields={'value': 1, '_id': 0})

        if _ is None:
            raise ParameterNotFound
        else:
            return _['value']

    def __init__(self):
        handlers_list = [
            ("/", handlers.MainHandler),
            ("/start", handlers.StartHandler),
            ("/auth/login", handlers.AuthHandler),
            ("/auth/logout", handlers.LogoutHandler),
            ("/user/([0-9a-fA-F]{24})(?:/(.*))?", handlers.UserHandler),
            ("/events/(.*)", handlers.EventsHandler),
            ("/matches/([0-9]+)", handlers.MatchHandler),
            ("/matches", handlers.MatchesHandler),
            ("/players", handlers.PlayersHandler),
            ("/page/(.*)", handlers.PageHandler)
        ]

        # Database
        try:
            client = MongoClient("localhost", 27017)
            self.db = client["Statsmile"]
        except ConnectionFailure:
            logging.fatal("Database connection can\'t be established, terminating!")
            exit(1)

        if not 'status' in self.db.collection_names():
            self.db.create_collection("status")
            self.db["status"].insert({"status": "api_dota", "value": "false", "time": datetime.now()})
            self.db["status"].insert({"status": "api_steam", "value": "false", "time": datetime.now()})

        # Secret
        self.db['settings'].ensure_index('key', unique=True)
        try:
            self.db["settings"].insert({"key": "cookie_secret",
                                        "value": "".join([choice(ascii_letters + digits) for _ in range(30)])},
                                       continue_on_error=True)
        except DuplicateKeyError:
            pass

        # Database initialization indexes
        self.db['matches'].ensure_index([("players.account_id", ASCENDING), ("game_mode", ASCENDING)])
        self.db['matches'].ensure_index([("start_time", DESCENDING)])

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
            ])['result']
        else:
            matches = self.db["users"].aggregate([
                {"$unwind": "$matches"},
                {"$project": {"matches": 1}},
                {"$group": {"_id": "$matches"}},
                {"$match": {"_id": {"$not": {"$in": complete["result"][0]["items"]}}}},
                {"$sort": {"_id": -1}},
                {"$limit": 1}
            ])['result']
        for mt in matches:
            IOLoop.instance().add_timeout((datetime.now() + timedelta(minutes=1)).timestamp(),
                                          partial(self.periodic_matches, mt["_id"]))

        settings = {
            "cookie_secret": self.get_cookies("cookie_secret"),
            "gzip": True,
            "debug": True,
            "template_path": os.path.join(os.path.dirname(__file__), "templates"),
            "static_path": os.path.join(os.path.dirname(__file__), "static"),
            "login_url": "/auth/login"
        }

        # Logger
        if settings["debug"]:
            logging.getLogger().setLevel(logging.DEBUG)
        self.logger = logging.getLogger("high log")

        super().__init__(handlers_list, **settings)

        self.listen(8888)
        self.logger.info("Statsmile server is started!")