#!/usr/bin/env python3

import os
import logging

from datetime import datetime, timedelta
from functools import partial

from tornado.gen import coroutine
from tornado.web import Application
from tornado.ioloop import IOLoop

from pymongo import ASCENDING, DESCENDING

from statsmile import handlers
from statsmile.common import getsecret, dbconn, update_match, update_user


class Statsmile(Application):

    @coroutine
    def user_update(self, user):
        logging.debug('Started updating %s user' % user['steamid'])

        yield update_user(self.db, user['steamid'])
        self.__update.remove(user['_id'])

        new_user = self.db['users'].find_one({'_id': {'$not': {'$in': self.__update}}},
                                             sort=[('update', ASCENDING)], limit=1)
        IOLoop.instance().add_timeout(new_user['update'].timestamp(), partial(self.user_update, new_user))

    @coroutine
    def match_update(self, match):
        logging.debug("Start receiving data match %s" % match)

        yield update_match(self.db, match)

        matches_db = self.db['matches'].aggregate([{'$group': {'_id': 'matches',
                                                               'items': {'$addToSet': '$match_id'}}}])['result'][0]
        new_matches = self.db['users'].aggregate([{'$unwind': '$matches'},
                                                  {'$project': {'matches': 1}},
                                                  {'$group': {'_id': '$matches'}},
                                                  {'$match': {'_id': {'$not': {'$in': matches_db['items']}}}},
                                                  {'$sort': {'_id': -1}},
                                                  {'$limit': 1}])['result']
        if new_matches:
            IOLoop.instance().add_timeout((datetime.now() + timedelta(seconds=10)).timestamp(),
                                          partial(self.match_update, new_matches[0]['_id']))
        else:
            IOLoop.instance().add_timeout((datetime.now() + timedelta(minutes=10)).timestamp(),
                                          partial(self.match_update, None))

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
        self.db['sessions'].ensure_index('last_activity', expireAfterSeconds=30 * 24 * 60 * 60)
        self.db['matches'].ensure_index([('players.account_id', ASCENDING), ('game_mode', ASCENDING)])
        self.db['matches'].ensure_index([('start_time', DESCENDING)])

        # Prepare status collection
        if not 'status' in self.db.collection_names():
            self.db['status'].insert([{'status': 'api_dota', 'value': 'false', 'time': datetime.now()},
                                      {'status': 'api_steam', 'value': 'false', 'time': datetime.now()}])

        # User profile updater
        self.__update = []

        users = self.db['users'].find({}).sort('update').limit(5)
        for it in users:
            IOLoop.instance().add_timeout(it['update'].timestamp(), partial(self.user_update, it))
            self.__update.append(it['_id'])

        # Match updater
        matches_db = self.db['matches'].aggregate(
            {'$group': {'_id': 'matches', 'items': {'$addToSet': '$match_id'}}})['result']
        if matches_db:
            getmatch = self.db['users'].aggregate([{"$unwind": "$matches"},
                                                   {"$project": {"matches": 1}},
                                                   {"$group": {"_id": "$matches"}},
                                                   {"$match": {"_id": {"$not": {"$in": matches_db[0]['items']}}}},
                                                   {"$sort": {"_id": -1}},
                                                   {"$limit": 1}])['result']
        else:
            getmatch = self.db['users'].aggregate([{"$unwind": "$matches"},
                                                   {"$project": {"matches": 1}},
                                                   {"$group": {"_id": "$matches"}},
                                                   {"$sort": {"_id": -1}},
                                                   {"$limit": 1}])['result']
        for mt in getmatch:
            IOLoop.instance().add_timeout((datetime.now() + timedelta(seconds=10)).timestamp(),
                                          partial(self.match_update, mt['_id']))

        settings = {
            'cookie_secret': getsecret.get_cookies(self.db, 'cookie_secret'),
            'gzip': True,
            'debug': True,
            'template_path': os.path.join(os.path.dirname(__file__), 'templates'),
            'static_path': os.path.join(os.path.dirname(__file__), 'static'),
            'login_url': "/auth/login"
        }

        if settings['debug']:
            logging.getLogger().setLevel(logging.DEBUG)

        super().__init__(handler_ls, **settings)

        self.listen(8888)
        logging.info('Statsmile server is started!')