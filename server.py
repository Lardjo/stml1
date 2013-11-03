#!/usr/bin/env python3

from tornado.ioloop import IOLoop
from tornado.options import define, parse_command_line
from statsmile import Statsmile

if __name__ == "__main__":

    define("mongo_host", default="mongodb://localhost:27017")
    define("mongo_db", default="Statsmile")

    parse_command_line()
    app = Statsmile()

    IOLoop.instance().start()