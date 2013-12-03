#!/usr/bin/env python3

from .base import BaseHandler
from bson import ObjectId


class MainHandler(BaseHandler):
    def get(self):
        settings = self.application.db['settings'].find_one({'key': "apikey", "value": {"$exists": "true"}})
        if settings is None:
            self.redirect("/start")
            return
        session = self.application.db["users"].find_one({"_id": ObjectId(self.current_user)})
        self.render("index.html", session=session)