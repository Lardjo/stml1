#!/usr/bin/env python3

from tornado.web import authenticated

from bson import ObjectId
from .base import BaseHandler


class SettingsHandler(BaseHandler):
    @authenticated
    def get(self):
        if not ObjectId.is_valid(self.current_user):
            return self.send_error(400)
        session = self.application.db["users"].find_one({"_id": ObjectId(self.current_user)})
        matches_on_base = self.application.db["matches"].find({"players.account_id": session["steamid_32"]}).count()
        try:
            progress = len(session["matches"])
        except KeyError:
            progress = 0
        self.render("user-settings.html", session=session, progress_on_base=matches_on_base, progress=progress)