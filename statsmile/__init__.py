#!/usr/bin/env python3
import sys

from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)
app.config.update(
    SECRET_KEY = 'development key',
    DEBUG = True
)

try:
    connection = MongoClient()
    db = connection.statsmile
    app.logger.info('Mongo database is connected')
except:
    app.logger.fatal('Mongo database connection can\'t be established')
    sys.exit(1)

import statsmile.pages
import statsmile.auth