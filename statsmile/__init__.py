#!/usr/bin/env python3
import logging
import os
import sys
import tornado.ioloop
import tornado.web

from functools import partial
from tornado import gen
from tornado.ioloop import IOLoop
from pymongo import MongoClient, ASCENDING
from pymongo.errors import ConnectionFailure
from statsmile import handlers
from statsmile.data import UpdateMatches


class Statsmile(tornado.web.Application):

    @gen.coroutine
    def periodic(self, user):
        self.logger.debug("Started updating '{}' user".format(user['steamid']))

        yield UpdateMatches(self.db, self.logger).update_matches_id(user['steamid'])
        self.__update.remove(user['_id'])

        new_match = self.db['users'].find_one({'_id': {'$not': {'$in': self.__update}}}, sort=[('next_update', ASCENDING)], limit=1)

        IOLoop.instance().add_timeout(new_match['next_update'].timestamp(), partial(self.periodic, new_match))
        self.__update.append(new_match['_id'])

    def __init__(self):

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
            ("/about", handlers.AboutHandler),
            ("/settings", handlers.SettingsHandler)]

        # Logger
        if settings['debug']:
            logging.getLogger().setLevel(logging.DEBUG)

        self.logger = logging.getLogger('log')
        self.logger.info("Log initialization complete")

        # Database
        try:
            client = MongoClient("localhost", 27017)
            self.logger.info("Mongo database is connected")
        except ConnectionFailure:
            self.logger.fatal("Database connection can\'t be established, terminating!")
            sys.exit(1)

        self.db = client['statsmile']

        # Settings
        if not 'settings' in self.db.collection_names():
            self.db.create_collection('settings')

        # Background updater
        self.__update = []

        users = self.db['users'].find({}).sort('next_update').limit(5)
        for it in users:
            IOLoop.instance().add_timeout(it['next_update'].timestamp(), partial(self.periodic, it))
            self.__update.append(it['_id'])

        super(Statsmile, self).__init__(handlers_list, **settings)
        self.listen(8888)
        self.logger.info("Statsmile server is started!")