#!/usr/bin/env python3

from .base import BaseHandler
from statsmile.common import libs


class HeroesHandler(BaseHandler):
    def get(self):
        session = self.application.db['sessions'].find_one({'_id': self.current_user})
        if session:
            session = self.application.db['users'].find_one({'_id': session['userid']})
        heroes = libs.heroes
        self.render("heroes.html", active="heroes", title="Heroes", session=session, heroes=heroes)


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