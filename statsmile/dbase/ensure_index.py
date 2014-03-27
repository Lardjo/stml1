#!/usr/bin/env python3

import logging

from pymongo import DESCENDING, ASCENDING


def create_index(db):
    """Create index

    Create ensure indexes when server is starting
    """
    logging.info('Scan indexes of database...')

    db.server.ensure_index('key', unique=True)

    # Matches
    db.matches.ensure_index('start_time', DESCENDING)
    db.matches.ensure_index('match_id', DESCENDING)
    db.matches.ensure_index('players.account_id', DESCENDING)
    db.matches.ensure_index('unregistered', sparse=True)
    db.matches.ensure_index('game_mode', ASCENDING)

    # Users
    db.users.ensure_index('winrate', DESCENDING)

    # Favorites
    db.favorites.ensure_index('id', DESCENDING)