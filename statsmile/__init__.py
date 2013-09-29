#!/usr/bin/env python3
import sys
import logging
import os
import tornado.ioloop
import tornado.web

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from statsmile import handlers

APIKEY = "E275AE4254A0C40A45E5EBEA4A793203"

class Statsmile(tornado.web.Application):
    """

    """
    def __init__(self):
        """
        Settings, handlers, connect to database
        """
        settings = {
            "cookie_secret": "#B&.Cu4QDe%{-m!`BbVa$YM+oXWk_5VT=iVEx@r97OBNflH>v_u]hcd?1#m.DF<",
            "gzip": True,
            "debug": True,
            "login_url": "/auth/login",
            "template_path": os.path.join(os.path.dirname(__file__), "templates"),
            "static_path": os.path.join(os.path.dirname(__file__), "static")}

        handlers_list = [
            ("/", handlers.MainHandler),
            ("/auth/login", handlers.AuthHandler),
            ("/auth/logout", handlers.LogoutHandler),
            ("/user/(.*)", handlers.UserHandler)]

        try:
            client = MongoClient("localhost", 27017)
            self.db = client["statsmile"]
            logging.info("Mongo database is connected")
        except ConnectionFailure:
            logging.fatal("Database connection can\'t be established, terminating!")
            sys.exit(1)

        super(Statsmile, self).__init__(handlers_list, **settings)
        self.listen(8888)
        logging.info("Statsmile server is started!")