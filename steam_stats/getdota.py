###
# Steam Stats (getdota.py)
# https://github.com/Lardjo/Steam-stats
#
# Copyright 2013, Konstantin N.
# All right reserved
#
# Hi, Valve! Your Steam Web API SUCKS! FF, GGWP.
# Proxy API required for private-key API with public data, my ass. (c)
###

import requests
import ConfigParser

from libs import dota2lib
from datetime import datetime
from getxml import download

# config
config = ConfigParser.ConfigParser()
config.read('bin/config.ini')
ZERO_KEY = int(config.get('steam', 'zerokey'))


class ParseError(Exception):
    pass


def last_match(userid=None, apikey=None):
    """Get Dota 2 Last Match id"""
    matchid = None
    options = {'format': 'XML', 'matches_requested': '1', 'account_id': userid, 'key': apikey}
    r = requests.get("https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/", params=options)
    root = download(r.url)

    try:
        status = root.find('status').text
        if status == "15":
            return 0
        else:
            pass
    except:
        raise

    for a in root.findall('./matches/match'):
        matchid = a.find('match_id').text

    options = {'format': 'XML', 'match_id': matchid, 'key': apikey}
    r = requests.get("https://api.steampowered.com/IDOTA2Match_570/GetMatchDetails/V001/", params=options)
    root = download(r.url)
    stats = match_stat(root)
    return stats


def match_stat(root=None):
    """Get Dota 2 Last Match Statistics"""
    hero = 0
    match = {'last_dota': {}}

    try:
        match['last_dota']['match_id'] = root.find('match_id').text
        match['last_dota']['radiant_win'] = root.find('radiant_win').text
        match['last_dota']['game_mode'] = root.find('game_mode').text
        match['last_dota']['cluster'] = root.find('cluster').text
        match['last_dota']['positive_votes'] = root.find('positive_votes').text
        match['last_dota']['negative_votes'] = root.find('negative_votes').text
    except:
        raise ParseError

    try:
        start_time = int(root.find('start_time').text)
        duration = int(root.find('duration').text)
        match['last_dota']['start_time'] = datetime.fromtimestamp(start_time).strftime('%d, %B %Y %H:%M:%S')
        match['last_dota']['duration'] = datetime.fromtimestamp(duration).strftime('%M:%S')
    except:
        raise ParseError

    try:
        first_blood = int(root.find('first_blood_time').text)
        match['last_dota']['first_blood'] = datetime.fromtimestamp(first_blood).strftime('%M:%S')
    except:
        pass

    a = int(match['last_dota']['game_mode'])
    if a in dota2lib.mode.keys():
        match['last_dota']['game_mode'] = dota2lib.mode[a]['name']
    else:
        pass

    a = int(match['last_dota']['cluster'])
    if a in dota2lib.cluster.keys():
        match['last_dota']['cluster'] = dota2lib.cluster[a]['name']
    else:
        pass

    for a in root.findall('./players/player'):
        try:
            account_id = a.find('account_id').text
            if account_id == "4294967295":
                hero += 1
                account_id = str(hero)
                nickname = "Anonymous"
            else:
                nickname = player_name(int(account_id))

            match['last_dota'][account_id] = {'player_slot': int(a.find('player_slot').text),
                                              'nickname': nickname,
                                              'hero_id': dota2lib.heroes[int(a.find('hero_id').text)]['name'],
                                              'hero_avatar': dota2lib.heroes[int(a.find('hero_id').text)]['avatar'],
                                              'kills': int(a.find('kills').text),
                                              'deaths': int(a.find('deaths').text),
                                              'assists': int(a.find('assists').text),
                                              'dn': int(a.find('denies').text),
                                              'gpm': int(a.find('gold_per_min').text),
                                              'xpm': int(a.find('xp_per_min').text),
                                              'lh': int(a.find('last_hits').text),
                                              'level': int(a.find('level').text),
                                              'item_0': dota2lib.items[int(a.find('item_0').text)]['avatar'],
                                              'item_1': dota2lib.items[int(a.find('item_1').text)]['avatar'],
                                              'item_2': dota2lib.items[int(a.find('item_2').text)]['avatar'],
                                              'item_3': dota2lib.items[int(a.find('item_3').text)]['avatar'],
                                              'item_4': dota2lib.items[int(a.find('item_4').text)]['avatar'],
                                              'item_5': dota2lib.items[int(a.find('item_5').text)]['avatar']}

        except:
            raise

    return match


def player_name(steam32=None):
    """STEAM API SUCKS!"""
    steam64 = steam32 + ZERO_KEY
    url = "http://steamcommunity.com/profiles/{0}?xml=1".format(steam64)
    root = download(url)
    try:
        name = root.find('steamID').text
    except:
        raise ParseError
    return name