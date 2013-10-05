#!/usr/bin/env python3
import logging
import os
import tornado.ioloop
import tornado.web

from statsmile import handlers
from statsmile.data import db


class Statsmile(tornado.web.Application):

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
            ("/user/(.*)", handlers.UserHandler),
            ("/privacy", handlers.PrivacyHandler),
            ("/about", handlers.AboutHandler),
            ("/settings", handlers.SettingsHandler)]

        self.db = db

        super(Statsmile, self).__init__(handlers_list, **settings)
        self.listen(8888)
        logging.info("Statsmile server is started!")