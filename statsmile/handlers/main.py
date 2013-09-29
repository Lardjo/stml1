#!/usr/bin/env python3
from .base import BaseHandler
from bson import ObjectId


class MainHandler(BaseHandler):
    """
    MainHandler
    """
    def get(self):
        if self.get_current_user():
            self.render("index.html",
                        session=self.application.db["users"].find_one({"_id": ObjectId(self.current_user)}))
        else:
            self.render("index.html", session=None)