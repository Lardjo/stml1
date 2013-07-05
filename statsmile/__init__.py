#!/usr/bin/env python3
import sys
import os
import configparser

from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)
app.config.update(
    SECRET_KEY = 'development key'
)

# silence gold
config = configparser.ConfigParser()
config.read(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'core', 'core.ini'))
STEAM_API_KEY = config.get('data', 'apikey')

try:
    connection = MongoClient()
    db = connection.statsmile
    app.logger.info('Mongo database is connected')
except:
    app.logger.fatal('Mongo database connection can\'t be established')
    sys.exit(1)

import statsmile.pages
import statsmile.auth