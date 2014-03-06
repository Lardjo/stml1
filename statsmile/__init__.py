#!/usr/bin/env python3

import os
import logging
import motor

from datetime import datetime, timedelta
from functools import partial

from tornado.gen import coroutine
from tornado.web import Application, asynchronous
from tornado.ioloop import IOLoop

from motor import Op
from pymongo import ASCENDING, DESCENDING
from pymongo.errors import ConnectionFailure

from statsmile import handlers
from statsmile.common import get_secret


class Statsmile(Application):

    def __init__(self):

        handlers_list = [
            (r'/', handlers.MainHandler),
            (r'/ws', handlers.WebSocketHandler),
            (r'/matches', handlers.MatchesHandler),
            (r'/matches/(.*)', handlers.MatchHandler)
        ]

        try:
            client = motor.MotorClient('localhost', 27017).open_sync()
            self.db = client['Statsmile']
            self.db_sync = client.sync_client()['Statsmile']
        except ConnectionFailure:
            logging.error('Could not connect to database. Exit.')
            exit(4)

        self.db['server'].ensure_index('key', unique=True)

        settings = {
            'cookie_secret': get_secret.get_cookies(self.db_sync, 'cookie_secret'),
            'gzip': True,
            'debug': True,
            'login_url': '/auth/login',
            'template_path': os.path.join(os.path.dirname(__file__), 'web', 'templates'),
            'static_path': os.path.join(os.path.dirname(__file__), 'web', 'static'),
        }

        if settings['debug']:
            logging.getLogger().setLevel(logging.DEBUG)

        super().__init__(handlers_list, **settings)

        self.listen(8888, xheaders=True)
        logging.info('Statsmile server is started!')