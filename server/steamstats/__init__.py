# steamstats\__init__.py
# All right reserved 2013

import os
import logging
import sys
import tornado.ioloop
import tornado.web

from pymongo import MongoClient
from server.steamstats import classes, config

class SteamStats(tornado.web.Application):
    """SteamStats"""
    def __init__(self):

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
            ]

        try:
            client = MongoClient("localhost", 27017)
            self.db = client["stats_base"]
            logging.info("MongoDB is connected")
        except:
            logging.fatal("Database connection can\'t be established, terminating")
            sys.exit(1)

        super(SteamStats, self).__init__(handlers, **settings)
        self.listen(8888)
        logging.info("Steam Stats server is started")