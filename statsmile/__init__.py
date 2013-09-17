#!/usr/bin/env python3
import sys

from flask import Flask
from pymongo import MongoClient, errors

# Steam API key #
#################
API_KEY = 'E275AE4254A0C40A45E5EBEA4A793203'

app = Flask(__name__)
app.config.update(
    SECRET_KEY='va1+wR&CgHJM/[9 kW9nBF-<_l)s/q|GTlyUHo-jfB/&OQtHW#Mn(s@S|!Y+WykT'
)

try:
    connection = MongoClient()
except errors.ConnectionFailure:
    sys.exit(1)

db = connection.statsmile

import statsmile.routes
import statsmile.auth