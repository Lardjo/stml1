#!/usr/bin/env python3

from .base import BaseHandler
from bson import ObjectId


class PageHandler(BaseHandler):
    def get(self, source):
        session = self.application.db["users"].find_one({"_id": ObjectId(self.current_user)})
        if source not in ('about', 'privacy', 'faq', 'status'):
            return self.send_error(404)
        elif source == "about":
            self.render("page.html", title="About", session=session)
        elif source == "privacy":
            self.render("page.html", title="Privacy Policy", session=session)
        elif source == "faq":
            self.render("page.html", title="FAQ", session=session)
        elif source == "status":
            status_dota = self.application.db["status"].find_one({"status": "api_dota"})
            status_steam = self.application.db["status"].find_one({"status": "api_steam"})
            self.render("page.html", title="Status", session=session, dota=status_dota, steam=status_steam)