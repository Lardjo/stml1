#!/usr/bin/env python3

from motor import Op
from tornado.gen import engine
from tornado.web import asynchronous, authenticated
from .base import BaseHandler


class SettingsHandler(BaseHandler):
    @authenticated
    @asynchronous
    @engine
    def get(self):
        session = yield Op(self.db['users'].find_one, {'_id': self.current_user['userid']})
        sessions, matches_on_base = yield [
            Op(self.db['sessions'].find({'userid': session['_id']}, sort=[('last_accessed', -1)]).to_list),
            Op(self.db['matches'].find({'players.account_id': session['steamid32']}).count)]

        try:
            progress = len(session['matches'])
        except KeyError:
            progress = 0

        self.render('user-settings.html', session=session, sessions=sessions, progress_on_base=matches_on_base,
                    progress=progress)