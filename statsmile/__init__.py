#!/usr/bin/env python3

import os
import logging

from tornado.web import Application

from statsmile import handlers
from statsmile.dbase import dbconn, ensure_index
from statsmile.common import get_secret, get_matches


class Statsmile(Application):

    def __init__(self):

        handlers_list = [
            (r'/', handlers.MainHandler),
            (r'/auth/login', handlers.AuthLoginHandler),
            (r'/auth/logout', handlers.AuthLogoutHandler),
        ]

        # Create db connection
        self.db, self.db_sync = dbconn.db_conn()

        # Check the index
        ensure_index.create_index(self.db)

        # Set settings
        settings = {
            'cookie_secret': get_secret.get_cookies(self.db_sync, 'cookie_secret'),
            'api_key': self.db_sync.server.find_one({'key': 'apikey'})['value'],
            'gzip': True,
            'debug': True,
            'login_url': '/auth/login',
            'template_path': os.path.join(os.path.dirname(__file__), 'web', 'templates'),
            'static_path': os.path.join(os.path.dirname(__file__), 'web', 'static'),
        }

        # Logging
        if settings['debug']:
            logging.getLogger().setLevel(logging.DEBUG)

        super().__init__(handlers_list, **settings)

        self.listen(8888, xheaders=True)
        logging.info('Statsmile server is started!')