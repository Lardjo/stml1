#!/usr/bin/env python3

import os
import motor
import logging

from datetime import datetime, timedelta
from functools import partial
from tornado.gen import coroutine
from tornado.web import Application, asynchronous
from tornado.ioloop import IOLoop
from motor import Op
from pymongo import ASCENDING, DESCENDING
from pymongo.errors import ConnectionFailure
from statsmile import handlers
from statsmile.common import getsecret, update_match, update_user, update_hero


class Statsmile(Application):

    @coroutine
    def user_update(self, user):

        logging.debug('Started updating %s user' % user['steamid'])

        try:
            yield update_user(self.db, user['steamid'])
        except Exception as e:
            logging.warning('Update user {} fails with error: {}'.format(user['steamid'], e))
            self.db['users'].update({'steamid': user['steamid']},
                                    {'$set': {'update': datetime.now() + timedelta(minutes=5)}})

        yield Op(self.db['users'].update, {'steamid': user['steamid']},
                 {'$set': {'update': datetime.now() + timedelta(minutes=5),
                           'last_update': datetime.now()}})

        self.__update.remove(user['_id'])

        new_user = yield Op(self.db['users'].find_one, {'_id': {'$nin': self.__update}},
                            sort=[('update', ASCENDING)], limit=1)

        IOLoop.instance().add_timeout(new_user['update'].timestamp(), partial(self.user_update, new_user))
        self.__update.append(new_user['_id'])

    @coroutine
    def match_update(self, match):
        logging.debug('Start receiving data match %s' % match)

        yield update_match(self.db, match)
        # Getting all id matches in db
        matches_db = yield Op(self.db['matches'].aggregate, [{'$group': {'_id': 'matches',
                                                                         'items': {'$addToSet': '$match_id'}}}])
        matches_db = matches_db['result'][0]['items']
        # Getting all id matches in user profiles and if new exists - get
        new_matches = yield Op(self.db['users'].aggregate,
                               [{'$unwind': '$matches'},
                                {'$project': {'matches': 1}},
                                {'$group': {'_id': '$matches'}},
                                {'$match': {'_id': {'$not': {'$in': matches_db}}}},
                                {'$sort': {'_id': -1}},
                                {'$limit': 1}])
        if new_matches['result']:
            IOLoop.instance().add_timeout((datetime.now() + timedelta(seconds=2)).timestamp(),
                                          partial(self.match_update, new_matches['result'][0]['_id']))
        else:
            IOLoop.instance().add_timeout((datetime.now() + timedelta(minutes=1)).timestamp(),
                                          partial(self.match_update, None))

    @coroutine
    def heroes_update(self, hero):
        logging.debug("Start update %s page" % hero['hero_id'])

        yield update_hero(self.db, hero)

        yield Op(self.db['heroes'].update, {'hero_id': hero['hero_id']},
                 {'$set': {'update': datetime.now() + timedelta(minutes=60),
                           'last_update': datetime.now()}})

        self.__update_hero.remove(hero['_id'])

        new_hero = yield Op(self.db['heroes'].find_one, {'_id': {'$not': {'$in': self.__update_hero}}},
                            sort=[('update', 1)], limit=1)

        IOLoop.instance().add_timeout(new_hero['update'].timestamp(), partial(self.heroes_update, new_hero))
        self.__update_hero.append(new_hero['_id'])

    def __init__(self):

        handler_ls = [
            (r'/', handlers.MainHandler),
            (r'/blog', handlers.BlogHandler),
            (r"/blog/([^/]+)", handlers.EntryHandler),
            (r"/postbox", handlers.ComposeHandler),
            (r'/status', handlers.StatusHandler),
            (r'/auth/login', handlers.AuthLoginHandler),
            (r'/auth/logout', handlers.AuthLogoutHandler),
            (r'/matches', handlers.MatchesHandler),
            (r'/players', handlers.PlayersHandler),
            (r'/page/(.*)', handlers.PagesHandler),
            (r'/user/([0-9a-fA-F]{24})', handlers.UserHandler),
            (r'/user/([0-9a-fA-F]{24})/matches', handlers.UserMatchesHandler),
            (r'/user/([0-9a-fA-F]{24})/heroes', handlers.UserHeroesHandler),
            (r'/user/([0-9a-fA-F]{24})/records', handlers.UserRecordsHandler),
            (r'/user/settings', handlers.SettingsHandler),
            (r'/user/bookmarks', handlers.BookmarksHandler),
            (r'/session/(.*)', handlers.SessionHandler),
            (r'/matches/([0-9]+)', handlers.MatchHandler),
            (r'/heroes', handlers.HeroesHandler),
            (r'/heroes/rating', handlers.HeroesTopHandler),
            (r'/heroes/(.*)', handlers.HeroHandler),
            (r'/events', handlers.EventsHandler)
        ]

        # Database connect
        try:
            client = motor.MotorClient('localhost', 27017).open_sync()
            self.db = client['Statsmile']
            self.db_sync = client.sync_client()['Statsmile']
        except ConnectionFailure:
            logging.error('Could not connect to Mongo DB. Exit')
            exit(4)

        # Ensure indexes
        self.db['server'].ensure_index('key', unique=True)
        self.db['sessions'].ensure_index('last_accessed', expireAfterSeconds=30 * 24 * 60 * 60)
        self.db['matches'].ensure_index([('players.account_id', ASCENDING), ('game_mode', ASCENDING)])
        self.db['matches'].ensure_index([('players.hero_id', ASCENDING), ('game_mode', ASCENDING)])
        self.db['matches'].ensure_index('start_time', DESCENDING)
        self.db['matches'].ensure_index('match_id', DESCENDING)
        self.db['heroes'].ensure_index('popularity', ASCENDING)
        self.db['heroes'].ensure_index('hero_id', ASCENDING)
        self.db['users'].ensure_index('steamid', ASCENDING)
        self.db['matches'].ensure_index('game_mode', ASCENDING)

        # User profile updater
        self.__update = []
        users = self.db_sync['users'].find({}).sort('update').limit(1)
        for it in users:
            IOLoop.instance().add_timeout(it['update'].timestamp(), partial(self.user_update, it))
            self.__update.append(it['_id'])

        # Heroes page updater
        self.__update_hero = []
        heroes = self.db_sync['heroes'].find({}).sort('update').limit(1)
        for hr in heroes:
            IOLoop.instance().add_timeout(hr['update'].timestamp(), partial(self.heroes_update, hr))
            self.__update_hero.append(hr['_id'])

        # Match updater
        matches_db = self.db_sync['matches'].aggregate(
            [{'$group': {'_id': 'matches', 'items': {'$addToSet': '$match_id'}}}])

        if matches_db['result']:
            getmatch = self.db_sync['users'].aggregate(
                [{"$unwind": "$matches"},
                 {"$project": {"matches": 1}},
                 {"$group": {"_id": "$matches"}},
                 {"$match": {"_id": {"$not": {"$in": matches_db['result'][0]['items']}}}},
                 {"$sort": {"_id": -1}},
                 {"$limit": 1}])
        else:
            getmatch = self.db_sync['users'].aggregate(
                [{"$unwind": "$matches"},
                 {"$project": {"matches": 1}},
                 {"$group": {"_id": "$matches"}},
                 {"$sort": {"_id": -1}},
                 {"$limit": 1}])

        if getmatch['result']:

            for mt in getmatch['result']:
                IOLoop.instance().add_timeout((datetime.now() + timedelta(seconds=2)).timestamp(),
                                              partial(self.match_update, mt['_id']))
        else:
            IOLoop.instance().add_timeout((datetime.now() + timedelta(seconds=10)).timestamp(),
                                          partial(self.match_update, None))

        settings = {
            'cookie_secret': getsecret.get_cookies(self.db_sync, 'cookie_secret'),
            'gzip': True,
            'debug': True,
            'template_path': os.path.join(os.path.dirname(__file__), 'templates'),
            'static_path': os.path.join(os.path.dirname(__file__), 'static'),
            'login_url': "/auth/login"
        }

        if settings['debug']:
            logging.getLogger().setLevel(logging.DEBUG)

        super().__init__(handler_ls, **settings)

        self.listen(8888, xheaders=True)
        logging.info('Statsmile server is started')