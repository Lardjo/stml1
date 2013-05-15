#!/usr/bin/env python3
# server\app.py
# All right reserved 2013
#
# This is main file
# Start server in here

import tornado.ioloop

from tornado.options import define, parse_command_line
from steamstats import UpdateServer

if __name__ == "__main__":

    define("mongo_host", default="mongodb://localhost:27017/")
    define("mongo_db", default="SteamStats")
    parse_command_line()
    app = UpdateServer()

    app.scheduler.start()
    tornado.ioloop.IOLoop.instance().start()