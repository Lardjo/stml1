#!/usr/bin/env python3

from ipwhois import IPWhois, IPDefinedError
from ipwhois.utils import get_countries

from .base import BaseHandler


class SettingsHandler(BaseHandler):

    def get(self):
        if not self.current_user:
            return self.send_error(403)
        session = self.application.db['sessions'].find_one({'_id': self.current_user})
        if not session:
            return self.send_error(400)
        session = self.application.db['users'].find_one({'_id': session['userid']})
        sessions = list(self.application.db['sessions'].find({'userid': session['_id']}).sort('last_accessed', -1))
        matches_on_base = self.application.db['matches'].find({'players.account_id': session['steamid32']}).count()

        try:
            progress = len(session['matches'])
        except KeyError:
            progress = 0

        countries = get_countries()

        for (country, offset) in enumerate(sessions):

            try:
                obj = IPWhois(offset['ip'])
                results = obj.lookup(False)
                sessions[offset]['country'] = countries[results['nets'][0]['country']]
            except IPDefinedError:
                sessions[country]['country'] = "Unknown Country"

        self.render('user-settings.html', active="settings", session=session, sessions=sessions,
                    progress_on_base=matches_on_base, progress=progress)