#!/usr/bin/env python3
"""
import uuid

from tornado import websocket

from .base import BaseHandler

cl = {}


class SocketHandler(websocket.WebSocketHandler, BaseHandler):

    def open(self):
        self.id = uuid.uuid4()
        if self.id not in cl:
            cl[self.id] = {'id': self.id}

    def on_close(self):
        if self.id in cl:
            del cl[self.id]
            """