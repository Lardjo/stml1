#!/usr/bin/env python3
from .base import BaseHandler
from bson import ObjectId

default = {
    'updates': 5
}

class SettingsHandler(BaseHandler):
    """
    SettingsHandler
    """
    def get(self):
        if self.get_current_user():
            self.render("settings.html",
                        session=self.application.db["users"].find_one({"_id": ObjectId(self.current_user)}))
        else:
            self.render("settings.html", session=None)