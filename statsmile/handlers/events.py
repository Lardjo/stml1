#!/usr/bin/env python3

from bson import ObjectId
from .base import BaseHandler


class EventsHandler(BaseHandler):
    def get(self, source):
        session = self.application.db['users'].find_one({"_id": ObjectId(self.current_user)})
        if source not in ('diretide', 'greeviling'):
            return self.send_error(404)
        elif source == "diretide":
            event = self.application.db["matches"].find({"game_mode": 7}).sort("match_id", -1).limit(20)
            self.render("event.html", title="Diretide", session=session, event=event)
        elif source == "greeviling":
            event = self.application.db["matches"].find({"game_mode": 9}).sort("match_id", -1).limit(20)
            self.render("event.html", title="The Greeviling", session=session, event=event)