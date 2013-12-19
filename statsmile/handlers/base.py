#!/usr/bin/env python3

import functools

from datetime import datetime
from bson import ObjectId

from motor import Op
from tornado import escape
from tornado.gen import engine, Task
from tornado.web import RequestHandler


def authenticated_asynchronous(f):

    @functools.wraps(f)
    @engine
    def wrapper(self, *args, **kwargs):
        self._auto_finish = False
        self.current_user = yield Task(self.get_current_user_asynchronous)
        if not self.current_user:
            pass
        else:
            self.db['sessions'].update({'_id': self.current_user['_id']}, {'$set': self.session_data()})
            f(self, *args, **kwargs)
    return wrapper


class BaseHandler(RequestHandler):
    @property
    def db(self):
        return self.application.db

    current_user = None

    @engine
    def get_current_user_asynchronous(self, callback):
        token = self.get_secure_cookie('user_session', None)
        if token:
            token = yield Op(self.db['sessions'].find_one, {'_id': ObjectId(escape.json_decode(token))})
        callback(token)

    def session_data(self):
        data = {'ip': self.request.remote_ip,
                'user_agent': self.request.headers.get("User-Agent", ""),
                'last_accessed': datetime.now()}
        return data