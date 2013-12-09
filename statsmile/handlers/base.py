#!/usr/bin/env python3

from tornado.web import RequestHandler
from tornado import escape

from datetime import datetime
from bson import ObjectId


class BaseHandler(RequestHandler):

    def get_current_user(self):
        token = self.get_secure_cookie('user_session')
        if not token:
            return None
        else:
            token = ObjectId(escape.json_decode(token))

        if not self.application.db['sessions'].find_one({'_id': token}):
            return None
        else:
            return token

    def session_data(self):
        data = {
            'ip': self.request.remote_ip,
            'user_agent': self.request.headers.get("User-Agent", ""),
            'last_accessed': datetime.now()
        }
        return data

    def prepare(self):
        token = self.get_current_user()
        if ObjectId.is_valid(token):
            if self.application.db['sessions'].find_one({'_id': token}):
                self.application.db['sessions'].update({'_id': token}, {'$set': self.session_data()})