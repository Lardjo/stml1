#!/usr/bin/env python3

from .base import BaseHandler
from bson import ObjectId


class MainHandler(BaseHandler):

    def get(self):
        session = self.application.db['sessions'].find_one({'_id': ObjectId(self.current_user)})
        if session:
            session = self.application.db['users'].find_one({'_id': session['userid']})
        self.render('index.html', title="Statsmile", session=session)