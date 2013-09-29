#!/usr/bin/env python3
import tornado.web
import tornado.escape

from datetime import datetime
from bson import ObjectId


class BaseHandler(tornado.web.RequestHandler):
    """
    Base?
    """
    def get_current_user(self):
        """
        user not auth, return None
        """
        jusr = self.get_secure_cookie("statsmile_user")
        if not jusr:
            return None
        return tornado.escape.json_decode(jusr)

    def session_now(self):
        """
        The last visit to the site
        """
        date = {"last_login": datetime.now()}
        return date

    def prepare(self):
        """
        Cookies
        """
        token = self.get_current_user()
        if ObjectId.is_valid(token):
            if self.application.db["users"].find_one({"_id": ObjectId(token)}):
                self.application.db["users"].update({"_id": ObjectId(token)}, {"$set": self.session_now()})