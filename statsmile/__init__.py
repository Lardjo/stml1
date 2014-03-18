#!/usr/bin/env python3

import os
import logging

from datetime import datetime, timedelta
from functools import partial

from motor import Op
from pymongo import DESCENDING

from tornado.gen import coroutine
from tornado.ioloop import IOLoop
from tornado.web import Application

from statsmile import handlers
from statsmile.dbase import dbconn, ensure_index
from statsmile.common import get_secret, get_matches
from statsmile.tasks import initiate


class Statsmile(Application):

    @coroutine
    def matches_upd(self, _seq_id):
        """Matches updater

        Matches Tasks
        """
        logging.debug('MATCH SEQ NUM: | %s | Start update...' % _seq_id)

        try:
            yield get_matches(self.db, _seq_id)
        except Exception as e:
            logging.warning('Error: %s' % e)

        logging.debug('MATCH SEQ NUM: | %s | Success!' % _seq_id)

        new_array = yield Op(self.db.server.find_one, {'key': 'last_match_update'}, limit=1)

        IOLoop.instance().add_timeout((datetime.now() + timedelta(seconds=1)).timestamp(),
                                      partial(self.matches_upd, new_array['value']))

    def __init__(self):

        handlers_list = [
            (r'/', handlers.MainHandler)
        ]

        # Create db connection
        self.db, self.db_sync = dbconn.db_conn()

        # Check the index
        ensure_index.create_index(self.db)

        # Set settings
        settings = {
            'cookie_secret': get_secret.get_cookies(self.db_sync, 'cookie_secret'),
            'gzip': True,
            'debug': True,
            'login_url': '/auth/login',
            'last_match_id': self.db_sync.server.find_one({'key': 'last_match_update'})['value'],
            'template_path': os.path.join(os.path.dirname(__file__), 'web', 'templates'),
            'static_path': os.path.join(os.path.dirname(__file__), 'web', 'static'),
        }

        # Logging
        if settings['debug']:
            logging.getLogger().setLevel(logging.DEBUG)

        # Initialize background update of matches
        logging.info('Initialize background update...')

        IOLoop.instance().add_timeout((datetime.now() + timedelta(seconds=1)).timestamp(),
                                      partial(self.matches_upd, settings['last_match_id']))

        super().__init__(handlers_list, **settings)

        self.listen(8888, xheaders=True)
        logging.info('Statsmile server is started!')