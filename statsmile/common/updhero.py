#!/usr/bin/env python3

import logging

from tornado import gen
from datetime import datetime, timedelta
from operator import itemgetter


@gen.coroutine
def update_hero(db, hero):

    items = db['matches'].aggregate([
        {'$match': {'players.hero_id': hero['hero_id'], 'game_mode': {"$nin": [7, 9, 15]}}},
        {'$unwind': '$players'},
        {'$match': {'players.hero_id': hero['hero_id']}},
        {'$project': {'item': '$players.items', 'count': {'$add': [1]}}},
        {'$unwind': '$item'},
        {'$group': {'_id': "$item", 'number': {'$sum': "$count"}}},
        {'$sort': {'number': -1}}
    ])

    top_heroes = db['matches'].aggregate([
        {'$match': {'game_mode': {"$nin": [7, 9, 15]}}},
        {'$unwind': '$players'},
        {'$project': {'hero_id': '$players.hero_id', 'count': {'$add': [1]}}},
        {'$group': {'_id': '$hero_id', 'number': {'$sum': '$count'}}},
        {'$sort': {'number': -1}}
    ])['result']

    try:
        pos = list(map(itemgetter('_id'), top_heroes)).index(hero['hero_id'])
        matches = top_heroes[pos]['number']
    except (ValueError, KeyError):
        pos = 0
        matches = 0

    db['heroes'].update({'hero_id': hero['hero_id']},
                        {'$set': {'popular_items': items['result'],
                                  'last_update': datetime.now(),
                                  'popularity': pos + 1,
                                  'matches': matches,
                                  'update': datetime.now() + timedelta(minutes=30)}})

    logging.info("Hero %s has been updated." % hero['hero_id'])