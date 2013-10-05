#!/usr/bin/env python3
import sys
import logging

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

try:
    client = MongoClient("localhost", 27017)
    logging.info("Mongo database is connected")
except ConnectionFailure:
    logging.fatal("Database connection can\'t be established, terminating!")
    sys.exit(1)

db = client["statsmile"]