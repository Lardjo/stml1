#!/usr/bin/env python3

from bson import ObjectId

from .base import BaseHandler


class HeroesHandler(BaseHandler):
    def get(self):
        session = self.application.db["users"].find_one({"_id": ObjectId(self.current_user)})
        self.render("heroes.html", session=session)