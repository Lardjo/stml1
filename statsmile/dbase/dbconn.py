#!/usr/bin/env python3

import logging

import motor

from pymongo.errors import ConnectionFailure


def db_conn():
    """Database connection

    Create connection with the Mongo Database
    """
    logging.info('Create the database connection...')

    try:
        client = motor.MotorClient('localhost', 27017).open_sync()
        db = client['Statsmile']
        db_sync = client.sync_client()['Statsmile']
        return db, db_sync
    except ConnectionFailure:
        logging.error('Could not connect to database. Exit...')
        exit(4)