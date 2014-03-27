#!/usr/bin/env python3

from .base import BaseHandler


class MainHandler(BaseHandler):
    def get(self):
        self.render('index.html')