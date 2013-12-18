#!/usr/bin/env python3

import math

from .base import BaseHandler
from bson import ObjectId
from pymongo import DESCENDING

from statsmile.common import libs


class EventsHandler(BaseHandler):
    def get(self, sid, page=1):
        session = self.application.db['sessions'].find_one({'_id': ObjectId(self.current_user)})
        if session:
            session = self.application.db['users'].find_one({'_id': session['userid']})
        pg = int(page)
        if not sid in ('wraithnight', 'diretide'):
            return self.send_error(404)
        elif sid == 'wraithnight':
            pages = self.application.db["matches"].find({"game_mode": 15}).count()
            max_pages = math.ceil(pages / 20)
            if pg > max_pages:
                return self.send_error(404)
            event = list(self.application.db["matches"].find({
                "game_mode": 15}).sort("start_time", DESCENDING).skip((pg-1)*20).limit(20))
            self.render('wraithnight.html', title="Wraith-Night", session=session, event=event, heroes=libs.heroes,
                        mode=libs.mode, cluster=libs.cluster, page=pg, max_pages=max_pages)
        else:
            return self.send_error(404)