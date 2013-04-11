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
    match = {'dota_players': [], 'dota_info': {}}

    try:
        match['dota_info']['match_id'] = root.find('match_id').text
        match['dota_info']['radiant_win'] = root.find('radiant_win').text
        match['dota_info']['game_mode'] = root.find('game_mode').text
        match['dota_info']['cluster'] = root.find('cluster').text
        match['dota_info']['positive_votes'] = root.find('positive_votes').text
        match['dota_info']['negative_votes'] = root.find('negative_votes').text
    except:
        raise ParseError

    try:
        start_time = int(root.find('start_time').text)
        duration = int(root.find('duration').text)
        match['dota_info']['start_time'] = datetime.fromtimestamp(start_time).strftime('%d, %B %Y %H:%M:%S')
        match['dota_info']['duration'] = datetime.fromtimestamp(duration).strftime('%M:%S')
    except:
        raise ParseError

    try:
        first_blood = int(root.find('first_blood_time').text)
        match['dota_info']['first_blood'] = datetime.fromtimestamp(first_blood).strftime('%M:%S')
    except:
        pass

    a = int(match['dota_info']['game_mode'])
    if a in dota2lib.mode.keys():
        match['dota_info']['game_mode'] = dota2lib.mode[a]['name']
    else:
        pass

    a = int(match['dota_info']['cluster'])
    if a in dota2lib.cluster.keys():
        match['dota_info']['cluster'] = dota2lib.cluster[a]['name']
    else:
        pass

    for a in root.findall('./players/player'):
        try:

            nickname = player_name(int(a.find('account_id').text))

            kills = float(a.find('kills').text)
            deaths = float(a.find('deaths').text)
            assists = float(a.find('assists').text)

            if kills > 0:
                wkills = round((kills * 100 / (kills + deaths + assists)), 3)
            else:
                wkills = 0
            if deaths > 0:
                wdeaths = round((deaths * 100 / (kills + deaths + assists)), 3)
            else:
                wdeaths = 0
            if assists > 0:
                wassists = round((assists * 100 / (kills + deaths + assists)), 3)
            else:
                wassists = 0

            match['dota_players'].append({'nickname': nickname,
                                     'hero_id': dota2lib.heroes[int(a.find('hero_id').text)]['name'],
                                     'hero_avatar': dota2lib.heroes[int(a.find('hero_id').text)]['avatar'],
                                     'kills': int(kills),
                                     'deaths': int(deaths),
                                     'assists': int(assists),
                                     'wkills': wkills,
                                     'wdeaths': wdeaths,
                                     'wassists': wassists,
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
                                     'item_5': dota2lib.items[int(a.find('item_5').text)]['avatar']})

        except:
            raise

    return match


def player_name(steam32=None):
    """STEAM API SUCKS!"""
    if steam32 == 4294967295:
        return "Anonymous"
    else:
        steam64 = steam32 + ZERO_KEY
    url = "http://steamcommunity.com/profiles/{0}?xml=1".format(steam64)
    root = download(url)
    try:
        name = root.find('steamID').text
    except:
        raise ParseError
    return name