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
from statsmile.common import getsecret, dbconn, update_match, update_user, update_hero


class Statsmile(Application):

    @coroutine
    def user_update(self, user):
        logging.debug('Started updating %s user' % user['steamid'])

        yield update_user(self.db, user['steamid'])
        self.__update.remove(user['_id'])

        new_user = self.db['users'].find_one({'_id': {'$not': {'$in': self.__update}}},
                                             sort=[('update', ASCENDING)], limit=1)
        IOLoop.instance().add_timeout(new_user['update'].timestamp(), partial(self.user_update, new_user))
        self.__update.append(new_user['_id'])

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
            IOLoop.instance().add_timeout((datetime.now() + timedelta(minutes=1)).timestamp(),
                                          partial(self.match_update, None))

    @coroutine
    def heroes_update(self, hero):
        logging.debug("Start update %s page" % hero['hero_id'])

        yield update_hero(self.db, hero)
        self.__update_hero.remove(hero['_id'])

        new_hero = self.db['heroes'].find_one({'_id': {'$not': {'$in': self.__update_hero}}},
                                              sort=[('update', ASCENDING)], limit=1)
        IOLoop.instance().add_timeout(new_hero['update'].timestamp(), partial(self.heroes_update, new_hero))
        self.__update_hero.append(new_hero['_id'])

    def __init__(self):

        handler_ls = [
            (r'/', handlers.MainHandler),
            (r'/status', handlers.StatusHandler),
            (r'/statistics', handlers.StatsHandler),
            (r'/auth/login', handlers.AuthLoginHandler),
            (r'/auth/logout', handlers.AuthLogoutHandler),
            (r'/matches', handlers.MatchesHandler),
            (r'/matches/page/([0-9]*)', handlers.MatchesHandler),
            (r'/players', handlers.PlayersHandler),
            (r'/page/(.*)', handlers.PagesHandler),
            (r'/user/([0-9a-fA-F]{24})', handlers.UserHandler),
            (r'/user/([0-9a-fA-F]{24})/matches', handlers.UserMatchesHandler),
            (r'/user/([0-9a-fA-F]{24})/records', handlers.UserRecordsHandler),
            (r'/user/([0-9a-fA-F]{24})/matches/page/([0-9]*)', handlers.UserMatchesHandler),
            (r'/user/settings', handlers.SettingsHandler),
            (r'/session/(.*)', handlers.SessionHandler),
            (r'/matches/([0-9]+)', handlers.MatchHandler),
            (r'/heroes', handlers.HeroesHandler),
            (r'/heroes/(.*)', handlers.HeroHandler),
            (r'/events/([^/]+)', handlers.EventsHandler),
            (r'/events/([^/]+)/page/([0-9]*)', handlers.EventsHandler)
        ]

        # Database connect
        self.db = dbconn.db_connection()

        # Ensure indexes
        self.db['server'].ensure_index('key', unique=True)
        self.db['sessions'].ensure_index('last_accessed', expireAfterSeconds=30 * 24 * 60 * 60)
        self.db['matches'].ensure_index([('players.account_id', ASCENDING), ('game_mode', ASCENDING)])
        self.db['matches'].ensure_index([('players.hero_id', ASCENDING), ('game_mode', ASCENDING)])
        self.db['matches'].ensure_index('start_time', DESCENDING)
        self.db['heroes'].ensure_index('popularity', ASCENDING)
        self.db['heroes'].ensure_index('hero_id', ASCENDING)
        self.db['users'].ensure_index('steamid', ASCENDING)
        self.db['matches'].ensure_index('game_mode', ASCENDING)

        # Prepare status collection
        if not 'status' in self.db.collection_names():
            self.db['status'].insert([{'status': 'api_dota', 'value': 'false', 'time': datetime.now()},
                                      {'status': 'api_steam', 'value': 'false', 'time': datetime.now()}])

        # User profile updater
        self.__update = []

        users = self.db['users'].find({}).sort('update').limit(2)
        for it in users:
            IOLoop.instance().add_timeout(it['update'].timestamp(), partial(self.user_update, it))
            self.__update.append(it['_id'])

        # Heroes page updater
        self.__update_hero = []

        heroes = self.db['heroes'].find({}).sort('update').limit(2)
        for hr in heroes:
            IOLoop.instance().add_timeout(hr['update'].timestamp(), partial(self.heroes_update, hr))
            self.__update_hero.append(hr['_id'])

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
        if getmatch:
            for mt in getmatch:
                IOLoop.instance().add_timeout((datetime.now() + timedelta(seconds=10)).timestamp(),
                                              partial(self.match_update, mt['_id']))
        else:
            IOLoop.instance().add_timeout((datetime.now() + timedelta(seconds=10)).timestamp(),
                                          partial(self.match_update, None))

        settings = {
            'cookie_secret': getsecret.get_cookies(self.db, 'cookie_secret'),
            'gzip': True,
            'debug': False,
            'template_path': os.path.join(os.path.dirname(__file__), 'templates'),
            'static_path': os.path.join(os.path.dirname(__file__), 'static'),
            'login_url': "/auth/login"
        }

        if settings['debug']:
            logging.getLogger().setLevel(logging.DEBUG)

        super().__init__(handler_ls, **settings)

        self.listen(8888, xheaders=True)
        logging.info('Statsmile server is started!')