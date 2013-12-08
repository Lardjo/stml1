#!/usr/bin/env python3

from .base import BaseHandler
from statsmile.common import libs


class HeroesHandler(BaseHandler):
    def get(self):
        session = self.application.db['sessions'].find_one({'_id': self.current_user})
        if session:
            session = self.application.db['users'].find_one({'_id': session['userid']})
        self.render("heroes.html", active="heroes", title="Heroes", session=session)


class HeroHandler(BaseHandler):
    def get(self, hero):
        hero = int(hero)
        if not hero in libs.heroes.keys():
            self.send_error(404)
        session = self.application.db['sessions'].find_one({'_id': self.current_user})
        if session:
            session = self.application.db['users'].find_one({'_id': session['userid']})
        hero = libs.heroes[hero]
        self.render("hero.html", active="heroes", session=session, hero=hero)