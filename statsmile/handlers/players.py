#!/usr/bin/env python3

from .base import BaseHandler
from pymongo import DESCENDING


class PlayersHandler(BaseHandler):
    def get(self):
        players = self.application.db['users'].find({}).sort('dota_count', DESCENDING).limit(20)
        session = self.application.db['sessions'].find_one({'_id': self.current_user})
        if session:
            session = self.application.db['users'].find_one({'_id': session['userid']})
        self.render('players.html', title="Statsmile / Players", session=session, players=players)