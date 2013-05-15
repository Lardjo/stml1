#!/usr/bin/env python3
# steamstats\__init__.py

import os
import logging
import sys
import tornado.ioloop
import tornado.web

from pymongo import MongoClient
from datetime import datetime
from bson import ObjectId
from . import classes
from . import config
from .classes import get


class SteamStats(tornado.web.Application):
    """
    Class SteamStats
    Main, main and main
    """
    def __init__(self):
        """
        Init function
        Settings, handlers, connect to db
        """
        settings = {
            "cookie_secret": config.SECRET_KEY,
            "gzip": True,
            "debug": True,
            "login_url": "/auth/login",
            "template_path": os.path.join(os.path.dirname(__file__), "templates"),
            "static_path": os.path.join(os.path.dirname(__file__), "static"),
            }

        handlers = [
            ("/", classes.MainHandler),
            ("/auth/login", classes.AuthHandler),
            ("/auth/logout", classes.LogoutHandler),
            ("/about", classes.AboutHandler),
            ('/user/(.*)', classes.UserHandler),
            ('/search', classes.SearchHandler),
            ]

        try:
            client = MongoClient("localhost", 27017)
            self.db = client["users_stats"]
            logging.info("MongoDB is connected")
        except:
            logging.fatal("Database connection can\'t be established, terminating")
            sys.exit(1)

        super(SteamStats, self).__init__(handlers, **settings)
        self.listen(8888)
        logging.info("Steam Stats server is started")


class UpdateServer(tornado.web.Application):
    """
    Main update class
    """
    def __init__(self):
        """
        Connect to database and run update server
        """
        try:
            client = MongoClient("localhost", 27017)
            self.db = client["users_stats"]
            logging.info("MongoDB is connected")
        except:
            logging.fatal("Database connection can\'t be established, terminating")
            sys.exit(1)

        super(UpdateServer, self).__init__()
        self.scheduler = tornado.ioloop.PeriodicCallback(self.update, 60000 * 60)
        self.listen(8150)
        logging.info("Update Server is started")


    def update(self):
        """
        Get and update
        """
        for users in self.db['sessions'].find():
            user = get.GetUserStats(users['steam']['steamID64'], config.API_KEY).dict
            user["last_update"] = datetime.now()
            self.db['sessions'].update({"_id": ObjectId(users["_id"])}, {"$set": user})
            logging.info("Update is complete for user %s", users["_id"])
