#!/usr/bin/env python3

from bson import ObjectId
from datetime import datetime

from tornado import escape
from tornado.web import RequestHandler

from statsmile.common.json_code import json_decode


class BaseHandler(RequestHandler):
    @property
    def db(self):
        return self.application.db

    @property
    def db_sync(self):
        return self.application.db_sync

    def get_current_user(self):
        token = self.get_secure_cookie('statsmile_session', None)

        if not token:
            return None
        else:
            token = ObjectId(escape.json_decode(token))

        if not ObjectId.is_valid(token):
            return None
        else:
            pass

        token = self.db_sync['sessions'].find_one({'_id': token}, {'_id': 1, 'userid': 1})

        if not token:
            return None
        else:
            return token

    def prepare(self):
        if self.current_user:
            self.db['sessions'].update({'_id': self.current_user['_id']}, {'$set': self.upd_session()})

        if self.request.headers.get('Content-Type') == 'application/json':
            self.json_args = json_decode(self.request.body.decode())

    def upd_session(self):
        data = {'ip': self.request.remote_ip,
                'user_agent': self.request.headers.get('User-Agent', ''),
                'last_accessed': datetime.now()}
        return data