#!/usr/bin/env python3

from bson import ObjectId
from .base import BaseHandler, authenticated_asynchronous
from motor import Op

import tornado.gen
import tornado.ioloop
import tornado.web


class MainHandler(BaseHandler):
    @tornado.web.asynchronous
    @tornado.gen.engine
    @authenticated_asynchronous
    def get(self):
        session = yield Op(self.db['users'].find_one, {'_id': self.current_user['userid']})
        self.render('index.html', title="Statsmile", session=None)