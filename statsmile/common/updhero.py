#!/usr/bin/env python3

import logging

from motor import Op
from tornado.gen import coroutine
from datetime import datetime, timedelta
from operator import itemgetter


@coroutine
def update_hero(db, hero):

    black_list = [7, 9, 15]

    items, top_heroes = yield [
        Op(db['matches'].aggregate,
           [{'$match': {'players.hero_id': hero['hero_id'], 'game_mode': {"$nin": black_list}}},
            {'$unwind': '$players'},
            {'$match': {'players.hero_id': hero['hero_id']}},
            {'$project': {'item': '$players.items', 'count': {'$add': [1]}}},
            {'$unwind': '$item'},
            {'$group': {'_id': "$item", 'number': {'$sum': "$count"}}},
            {'$sort': {'number': -1}}]),
        Op(db['matches'].aggregate,
           [{'$match': {'game_mode': {"$nin": [7, 9, 15]}}},
            {'$unwind': '$players'},
            {'$project': {'hero_id': '$players.hero_id', 'count': {'$add': [1]}}},
            {'$group': {'_id': '$hero_id', 'number': {'$sum': '$count'}}},
            {'$sort': {'number': -1}}])]

    try:
        pos = list(map(itemgetter('_id'), top_heroes['result'])).index(hero['hero_id'])
        matches = top_heroes['result'][pos]['number']
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