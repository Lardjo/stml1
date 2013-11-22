#!/usr/bin/env python3

from bson import ObjectId
from .base import BaseHandler


class GreevilingHandler(BaseHandler):
    def get(self):
        session = self.application.db['users'].find_one({"_id": ObjectId(self.current_user)})
        greeviling = self.application.db["matches"].find({"game_mode": 9}).sort("match_id", -1).limit(20)
        self.render("greeviling.html", session=session, greeviling=greeviling)