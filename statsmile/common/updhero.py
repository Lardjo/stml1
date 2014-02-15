#!/usr/bin/env python3

import logging
import time

from motor import Op
from tornado.gen import coroutine
from datetime import datetime, timedelta
from operator import itemgetter


@coroutine
def update_hero(db, hero):

    black_list = [7, 9, 15]
    current_time = time.time()

    items, top_heroes, top_heroes_week, top_heroes_month = yield [
        Op(db['matches'].aggregate,
           [{'$match': {'players.hero_id': hero['hero_id'], 'game_mode': {"$nin": black_list}}},
            {'$unwind': '$players'},
            {'$match': {'players.hero_id': hero['hero_id']}},
            {'$project': {'item': '$players.items', 'count': {'$add': [1]}}},
            {'$unwind': '$item'},
            {'$group': {'_id': "$item", 'number': {'$sum': "$count"}}},
            {'$sort': {'number': -1}}]),
        Op(db['matches'].aggregate,
           [{'$match': {'game_mode': {"$nin": black_list}}},
            {'$unwind': '$players'},
            {'$project': {'hero_id': '$players.hero_id', 'count': {'$add': [1]}}},
            {'$group': {'_id': '$hero_id', 'number': {'$sum': '$count'}}},
            {'$sort': {'number': -1}}]),
        Op(db['matches'].aggregate,
           [{'$match': {'start_time': {'$gte': current_time - 604800, '$lt': current_time},
                        'game_mode': {"$nin": black_list}}},
            {'$unwind': '$players'},
            {'$project': {'hero_id': '$players.hero_id', 'count': {'$add': [1]}}},
            {'$group': {'_id': '$hero_id', 'number': {'$sum': '$count'}}},
            {'$sort': {'number': -1}}]),
        Op(db['matches'].aggregate,
           [{'$match': {'start_time': {'$gte': current_time - 2629743, '$lt': current_time},
                        'game_mode': {"$nin": black_list}}},
            {'$unwind': '$players'},
            {'$project': {'hero_id': '$players.hero_id', 'count': {'$add': [1]}}},
            {'$group': {'_id': '$hero_id', 'number': {'$sum': '$count'}}},
            {'$sort': {'number': -1}}])]

    # Remove zero point
    try:
        pos = list(map(itemgetter('_id'), top_heroes['result'])).index(0)
        top_heroes['result'].pop(pos)
    except ValueError:
        pass
    try:
        pos_week = list(map(itemgetter('_id'), top_heroes_week['result'])).index(0)
        top_heroes_week['result'].pop(pos_week)
    except ValueError:
        pass
    try:
        pos_month = list(map(itemgetter('_id'), top_heroes_month['result'])).index(0)
        top_heroes_month['result'].pop(pos_month)
    except ValueError:
        pass

    try:
        pos = list(map(itemgetter('_id'), top_heroes['result'])).index(hero['hero_id'])
        matches = top_heroes['result'][pos]['number']
    except (ValueError, KeyError):
        pos = len(top_heroes['result'])
        matches = 0

    try:
        pos_week = list(map(itemgetter('_id'), top_heroes_week['result'])).index(hero['hero_id'])
        matches_week = top_heroes_week['result'][pos_week]['number']
    except (ValueError, KeyError):
        pos_week = len(top_heroes_week['result'])
        matches_week = 0

    try:
        pos_month = list(map(itemgetter('_id'), top_heroes_month['result'])).index(hero['hero_id'])
        matches_month = top_heroes_month['result'][pos_month]['number']
    except (ValueError, KeyError):
        pos_month = len(top_heroes_month['result'])
        matches_month = 0

    # Total Hours
    hours = yield Op(db['matches'].aggregate,
                     [{'$match': {'players.hero_id': hero['hero_id'], 'game_mode': {'$nin': black_list}}},
                      {'$group': {'_id': 'None', 'sum': {'$sum': '$duration'}}}])

    # Popularity WEEK
    pop = []
    days = current_time

    for day in range(7):

        matches_all, hero_matches = yield [
            Op(db['matches'].find({'start_time': {'$gte': days - 86400, '$lt': days},
                                   'game_mode': {'$nin': black_list},
                                   'players.hero_id': {'$nin': [0]}}).count),
            Op(db['matches'].find({'start_time': {'$gte': days - 86400, '$lt': days},
                                   'players.hero_id': hero['hero_id'],
                                   'game_mode': {'$nin': black_list}}).count)]
        if hero_matches != 0:
            popularity = (hero_matches / matches_all) * 100
        else:
            popularity = 0

        pop.append(popularity)
        days = (days - 86400)

    db['heroes'].update({'hero_id': hero['hero_id']},
                        {'$set': {'popular_items': items['result'],
                                  'popularity': pos + 1,
                                  'popularity_week': pos_week + 1,
                                  'popularity_month': pos_month + 1,
                                  'popularity_graph': pop[::-1],
                                  'total_hours': hours['result'][0]['sum'],
                                  'average': hours['result'][0]['sum'] / matches,
                                  'matches': matches,
                                  'matches_week': matches_week,
                                  'matches_month': matches_month}})

    logging.info("Hero %s has been updated." % hero['hero_id'])