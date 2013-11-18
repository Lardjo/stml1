#!/usr/bin/env python3

from .base import BaseHandler
from bson import ObjectId


class AboutHandler(BaseHandler):
    def get(self):
        session = self.application.db["users"].find_one({"_id": ObjectId(self.current_user)})
        self.render("about.html", session=session)