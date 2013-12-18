#!/usr/bin/env python3

from .base import BaseHandler
from statsmile.common import libs
from pymongo import ASCENDING


class HeroesHandler(BaseHandler):
    def get(self):
        session = self.application.db['sessions'].find_one({'_id': self.current_user})
        if session:
            session = self.application.db['users'].find_one({'_id': session['userid']})
        heroes = libs.heroes
        popularity = self.application.db['heroes'].find({}, {'hero_id': 1, 'matches': 1}).sort('popularity', ASCENDING)
        self.render("heroes.html", active="heroes", title="Heroes", session=session, heroes=heroes, top=popularity)


class HeroHandler(BaseHandler):
    def get(self, hero):
        hero = int(hero)
        if not hero in libs.heroes_info.keys():
            self.send_error(404)
        session = self.application.db['sessions'].find_one({'_id': self.current_user})
        if session:
            session = self.application.db['users'].find_one({'_id': session['userid']})
        stats = self.application.db['heroes'].find_one({'hero_id': hero})
        hero_info = libs.heroes_info[hero]
        self.render("hero.html", session=session, hero=hero_info, stats=stats, items=libs.items)