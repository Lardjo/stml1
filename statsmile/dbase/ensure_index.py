#!/usr/bin/env python3

import logging

from pymongo import DESCENDING


def create_index(db):
    """Create index

    Create ensure indexes when server is starting
    """
    logging.info('Scan indexes of database...')

    db.server.ensure_index('key', unique=True)
    db.matches.ensure_index('start_time', DESCENDING)
    db.matches.ensure_index('match_id', DESCENDING)