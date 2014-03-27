#!/usr/bin/env python3

import os
import logging

from datetime import datetime, timedelta
from functools import partial

from motor import Op
from pymongo import ASCENDING

from tornado.web import Application
from tornado.gen import coroutine
from tornado.ioloop import IOLoop

from statsmile import api
from statsmile.dbase import dbconn, ensure_index
from statsmile.common import get_secret, get_matches, user_update


class Statsmile(Application):

    @coroutine
    def user_update(self, user):
        """User Update

        Periodical function for update user profiles
        """
        logging.debug('Updating %s user' % user['id'])

        try:
            yield user_update(self.db, self.settings['api_key'], user['claimed_id'], user['id'])
        except Exception as e:

            logging.warning('Update user %s occurred error: %s' % (user['_id'], e))
            yield Op(self.db.users.update, {'_id': user['_id']},
                     {'$set': {'update': datetime.now() + timedelta(minutes=10)}})

        yield Op(self.db.users.update, {'_id': user['_id']},
                 {'$set': {'update': datetime.now() + timedelta(minutes=10), 'last': datetime.now()}})

        self.__update.remove(user['_id'])

        user = yield Op(self.db.users.find_one, {'_id': {'$nin': self.__update}},
                        sort=[('update', ASCENDING)], limit=1)

        IOLoop.instance().add_timeout(user['update'].timestamp(), partial(self.user_update, user))
        self.__update.append(user['_id'])

    def __init__(self):

        handlers_list = [
            (r'/', api.MainHandler),
            (r'/auth/login', api.AuthLoginHandler),
            (r'/auth/logout', api.AuthLogoutHandler),
            (r'/auth', api.AuthHandler),
            (r'/players', api.PlayersHandler),
            (r'/players/(.*)', api.PlayerHandler),
            (r'/matches', api.MatchesHandler),
            (r'/matches/(.*)', api.MatchHandler)
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

        # Users updater
        self.__update = []
        users = self.db_sync.users.find({}).sort('update').limit(1)

        for it in users:
            IOLoop.instance().add_timeout(it['update'].timestamp(), partial(self.user_update, it))
            self.__update.append(it['_id'])

        super().__init__(handlers_list, **settings)

        self.listen(8888, xheaders=True)
        logging.info('Statsmile server is started!')