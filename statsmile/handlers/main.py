#!/usr/bin/env python3

from tornado.gen import engine
from tornado.web import asynchronous

from .base import BaseHandler


class MainHandler(BaseHandler):
    @asynchronous
    @engine
    def get(self):
        self.render('index.html')