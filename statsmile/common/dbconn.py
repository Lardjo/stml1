#!/usr/bin/env python3

import logging
import motor


def db_connection():
    db = motor.MotorClient('localhost', 27017).open_sync()['Statsmile']
    logging.info('Database is successfully connected')
    return db