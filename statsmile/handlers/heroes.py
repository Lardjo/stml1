#!/usr/bin/env python3

from motor import Op
from tornado.gen import engine
from tornado.web import asynchronous
from .base import BaseHandler
from statsmile.common import libs


class HeroesHandler(BaseHandler):
    @asynchronous
    @engine
    def get(self):
        session = None
        if self.current_user:
            session = yield Op(self.db['users'].find_one, {'_id': self.current_user['userid']})
        self.render("heroes.html", title="Heroes", session=session, heroes=libs.heroes)


class HeroesTopHandler(BaseHandler):
    @asynchronous
    @engine
    def get(self):
        session = None
        if self.current_user:
            session = yield Op(self.db['users'].find_one, {'_id': self.current_user['userid']})

        period = self.get_argument('period', 'all')

        if not period in ('all', 'month', 'week'):
            return self.send_error(404)

        if period == 'month':
            cursor = self.db['heroes'].find({}, {'hero_id': 1,
                                                 'matches_month': 1,
                                                 'popularity_month': 1}, sort=[('popularity_month', 1)], limit=115)
            popularity = yield Op(cursor.to_list)
        elif period == 'week':
            cursor = self.db['heroes'].find({}, {'hero_id': 1,
                                                 'matches_week': 1,
                                                 'popularity_week': 1}, sort=[('popularity_week', 1)], limit=115)
            popularity = yield Op(cursor.to_list)
        else:
            cursor = self.db['heroes'].find({}, {'hero_id': 1,
                                                 'matches': 1,
                                                 'popularity': 1}, sort=[('popularity', 1)], limit=115)
            popularity = yield Op(cursor.to_list)

        self.render("heroes.html", title="Heroes / Rating", session=session, period=period,
                    heroes=libs.heroes, top=popularity)


class HeroHandler(BaseHandler):
    @asynchronous
    @engine
    def get(self, hero):
        session = None
        if self.current_user:
            session = yield Op(self.db['users'].find_one, {'_id': self.current_user['userid']})
        hero = int(hero)
        if not hero in libs.heroes_info.keys():
            return self.send_error(404)
        stats = yield Op(self.application.db['heroes'].find_one, {'hero_id': hero})

        cursor = self.db['matches'].find({'players.hero_id': hero, 'game_mode': {'$nin': [7, 9, 15]}},
                                         {'game_mode': 1, 'start_time': 1, 'duration': 1, 'cluster': 1,
                                          'match_id': 1, 'radiant_win': 1, 'lobby_type': 1,
                                          'players': {'$elemMatch': {'hero_id': hero}}},
                                         sort=[('start_time', -1)], limit=5)

        matches = yield Op(cursor.to_list)

        hero_info = libs.heroes_info[hero]
        self.render("hero.html", session=session, hero=hero_info, stats=stats, items=libs.items, heroes=libs.heroes,
                    mode=libs.mode, matches=matches)