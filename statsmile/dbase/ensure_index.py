#!/usr/bin/env python3

import logging

from pymongo import DESCENDING, ASCENDING


def create_index(db):
    """Create index

    Create ensure indexes when server is starting
    """
    logging.info('Scan indexes of database...')

    db.server.ensure_index('key', unique=True)
    db.matches.ensure_index('start_time', DESCENDING)
    db.matches.ensure_index('match_id', DESCENDING)
    db.matches.ensure_index('players.account_id', DESCENDING)
    db.matches.ensure_index('unregistered', sparse=True)
    db.matches.ensure_index('game_mode', ASCENDING)
    db.users.ensure_index('win_rate', DESCENDING)