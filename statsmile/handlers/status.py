#!/usr/bin/env python3

from motor import Op

from tornado.gen import engine
from tornado.web import asynchronous

from .base import BaseHandler
from statsmile.common.json_code import json_encode


class StatusHandler(BaseHandler):
    def prepare(self):
        super().prepare()
        self.set_header('Content-Type', 'application/json; charset=UTF-8')

    @asynchronous
    @engine
    def get(self):
        cursor = self.db['status'].find({}, limit=5)
        status = yield Op(cursor.to_list)
        self.write(json_encode(status[0]))
        self.finish()