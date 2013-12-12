#!/usr/bin/env python3

from .base import BaseHandler


class PagesHandler(BaseHandler):
    def get(self, source):
        session = self.application.db['sessions'].find_one({'_id': self.current_user})
        if session:
            session = self.application.db['users'].find_one({'_id': session['userid']})
        if source not in ('about', 'privacy', 'faq', 'status', 'license'):
            return self.send_error(404)
        elif source == "about":
            self.render("pages.html", title="About", active="page", session=session)
        elif source == "privacy":
            self.render("pages.html", title="Privacy Policy", active="page", session=session)
        elif source == "faq":
            self.render("pages.html", title="FAQ", active="page", session=session)
        elif source == "license":
            self.render("pages.html", title="License", active="page", session=session)
        elif source == "status":
            st_dota = self.application.db['status'].find_one({'status': 'api_dota'})
            st_steam = self.application.db['status'].find_one({'status': 'api_steam'})
            self.render("pages.html", title="Status", session=session, active="page", dota=st_dota, steam=st_steam)