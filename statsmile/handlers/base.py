#!/usr/bin/env python3

import tornado.web
import tornado.escape

from datetime import datetime
from bson import ObjectId


class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        jusr = self.get_secure_cookie("statsmile_user")
        if not jusr:
            return None
        return tornado.escape.json_decode(jusr)

    def session_now(self):
        date = {"last_login": datetime.now()}
        return date

    def prepare(self):
        token = self.get_current_user()
        if ObjectId.is_valid(token):
            if self.application.db["users"].find_one({"_id": ObjectId(token)}):
                self.application.db["users"].update({"_id": ObjectId(token)}, {"$set": self.session_now()})