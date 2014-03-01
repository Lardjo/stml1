#!/usr/bin/env python3

from motor import Op

from tornado.gen import engine
from tornado.web import asynchronous

from .base import BaseHandler


class MainHandler(BaseHandler):
    def get(self):
        self.render('index.html')