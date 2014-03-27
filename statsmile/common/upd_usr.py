#!/usr/bin/env python3

import logging

from datetime import datetime

from motor import Op

from tornado.gen import coroutine
from tornado.escape import json_decode
from tornado.httputil import url_concat
from tornado.httpclient import AsyncHTTPClient

from .get_matches_id import get_matches_id
from .get_matches import get_matches


@coroutine
def user_update(db, key, _id, _id32):
    """User update

    Function for getting user profile, update stats and info

    Part 1. Getting latest 500 matches. Selection only ranked matches and add if not in database
    """

    matches = yield get_matches_id(key, _id)

    yield get_matches(db, key, matches)

    # Favorites heroes
    favorites = yield Op(db.matches.aggregate,
                         [{'$match': {'players.account_id': _id32, 'unregistered': {'$exists': False}}},
                          {'$unwind': '$players'},
                          {'$match': {'players.account_id': _id32}},
                          {'$project': {'_id': 0, 'radiant_win': 1, 'slot': '$players.player_slot',
                                        'players.player_slot': 1, 'players.hero_id': 1, 'players.account_id': 1,
                                        'players.kills': 1, 'players.deaths': 1, 'players.assists': 1,
                                        'players.count': {'$add': [1]}}},
                          {'$group': {'_id': '$players.hero_id',
                                      'wins': {
                                          '$sum': {
                                              '$cond': [{'$or': [{'$and': [{'$eq': ['$radiant_win', True]},
                                                                           {'$lt': ['$slot', 5]}]},
                                                                 {'$and': [{'$eq': ['$radiant_win', False]},
                                                                           {'$gt': ['$slot', 127]}]}]}, 1, 0]}},
                                      'matches': {"$sum": "$players.count"},
                                      'kills': {"$sum": "$players.kills"},
                                      'deaths': {"$sum": "$players.deaths"},
                                      'assists': {"$sum": "$players.assists"}}},
                          {'$sort': {'matches': -1}},
                          {'$limit': 115}])

    db.favorites.update({'steam_id32': _id32}, {'$set': {'favorites': favorites['result']}}, upsert=True)

    url = url_concat('https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/', {'key': key, 'steamids': _id})

    http_client = AsyncHTTPClient()
    response = yield http_client.fetch(url)

    if response.error:
        logging.warning('User %s has not updated. Error: %s. Code: %s' % (_id, response.error, response.code))
        db.status.update({'key': 'steam_api'}, {'$set': {'value': False, 'time': datetime.now()}})

    else:
        user = json_decode(response.body)['response']['players'][0]
        user = {'persona_name': user['personaname'],
                'profile_url': user['profileurl'],
                'avatar': user['avatarfull'],
                'real_name': user.get('realname', None)}
        db.users.update({'steam_id': _id}, {'$set': user})
        db.status.update({'key': 'steam_api'}, {'$set': {'value': True, 'time': datetime.now()}})

    matches_array = yield Op(db.matches.find({'players.account_id': _id32, 'unregistered': {'$exists': False}},
                                             {'radiant_win': 1,
                                              'players': {'$elemMatch': {'account_id': _id32}}}, limit=5000).to_list)
    matches_count = int(len(matches_array))
    matches_win = 0
    matches_loses = 0

    for match in matches_array:
        if match['radiant_win'] and match['players'][0]['player_slot'] < 5:
            matches_win += 1
        elif (not match['radiant_win']) and match['players'][0]['player_slot'] > 5:
            matches_win += 1
        else:
            matches_loses += 1

    win_rate = round((matches_win / matches_count * 100), 2)

    db.users.update({'steam_id': _id}, {'$set': {'matches_count': matches_count,
                                                 'wins': matches_win,
                                                 'loses': matches_loses,
                                                 'win_rate': float(win_rate)}})

    logging.info('User %s update complete!' % _id32)
