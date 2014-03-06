#!/usr/bin/env python3

import logging
import tornado.websocket

from tornado.ioloop import IOLoop
from datetime import datetime, timedelta
from functools import partial

clients = dict()


class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def open(self, *args):
        self.id = self.get_argument('id')
        self.stream.set_nodelay(True)
        clients[self.id] = {'id': self.id, 'object': self}

    def on_message(self, message):
        logging.info('Start recalculate')
        self.write_message(u'Start recalculate statistics for %s user... It can take 1-2 minutes...' % message)
        IOLoop.instance().add_timeout((datetime.now() + timedelta(seconds=10)).timestamp(),
                                      partial(self.test_delay, message))

    def on_close(self):
        if self.id in clients:
            del clients[self.id]

    def test_delay(self, mess):
        self.write_message(u'You said: ' + mess)