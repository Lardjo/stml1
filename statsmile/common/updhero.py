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
    ])

    try:
        pos = list(map(itemgetter('_id'), top_heroes['result'])).index(hero['hero_id']) + 1
    except ValueError:
        pos = 112

    db['heroes'].update({'hero_id': hero['hero_id']}, {'$set': {'popularity': pos}})
    db['heroes'].update({'hero_id': hero['hero_id']},
                        {'$set': {"popular_items": items['result']}}, upsert=True)
    db['heroes'].update({'hero_id': hero['hero_id']},
                        {'$set': {'last_update': datetime.now()}}, upsert=True)
    db['heroes'].update({'hero_id': hero['hero_id']},
                        {'$set': {'update': datetime.now() + timedelta(minutes=15)}}, upsert=True)

    logging.debug("Hero %s has been updated." % hero['hero_id'])