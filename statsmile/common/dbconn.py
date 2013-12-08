#!/usr/bin/env python3

import logging

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure


def db_connection():
    try:
        client = MongoClient('localhost', 27017)
        db = client['Statsmile']
        return db
    except ConnectionFailure:
        logging.fatal("Database connection can\'t be established, terminating!")
        exit(1)