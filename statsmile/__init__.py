#!/usr/bin/env python3

import os
import logging

from tornado.web import Application

from pymongo import ASCENDING, DESCENDING

from statsmile import handlers
from statsmile.common import getsecret, dbconn


class Statsmile(Application):

    def __init__(self):

        handler_ls = [
            (r'/', handlers.MainHandler),
            (r'/auth/login', handlers.AuthLoginHandler),
            (r'/auth/logout', handlers.AuthLogoutHandler)
        ]

        # Database connect
        self.db = dbconn.db_connection()

        # Ensure indexes
        self.db['server'].ensure_index('key', unique=True)
        self.db['matches'].ensure_index([("players.account_id", ASCENDING), ("game_mode", ASCENDING)])
        self.db['matches'].ensure_index([("start_time", DESCENDING)])

        settings = {
            "cookie_secret": getsecret.get_cookies(self.db, 'cookie_secret'),
            "gzip": True,
            "debug": True,
            "template_path": os.path.join(os.path.dirname(__file__), "templates"),
            "static_path": os.path.join(os.path.dirname(__file__), "static"),
            "login_url": "/auth/login"
        }

        super().__init__(handler_ls, **settings)

        self.listen(8888)
        logging.info("Statsmile server is started!")