#!/usr/bin/env python3

from .base import BaseHandler


class StatusHandler(BaseHandler):
    def get(self):
        session = self.application.db['sessions'].find_one({'_id': self.current_user})
        if session:
            session = self.application.db['users'].find_one({'_id': session['userid']})
        st_dota = self.application.db['status'].find_one({'status': 'api_dota'})
        st_steam = self.application.db['status'].find_one({'status': 'api_steam'})
        self.render("status.html", title="Status", session=session, dota=st_dota, steam=st_steam)