#!/usr/bin/env python3
# steamstats\__init__.py

import os
import logging
import sys
import tornado.ioloop
import tornado.web

from pymongo import MongoClient
from . import classes
from . import config


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