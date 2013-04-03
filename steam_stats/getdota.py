from libs import dota2lib
from datetime import datetime
from getxml import get_xml

url = {"GET_ID": "https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/?format=XML&matches_requested=1&account_id={0}&key={1}",
       "GET_INFO": "https://api.steampowered.com/IDOTA2Match_570/GetMatchDetails/V001/?format=XML&match_id={0}&key={1}"}


class ParseError(Exception):
    pass


def last_match(userid=None, apikey=None):
    """Get Dota 2 Last Match id"""
    matchid = None
    root = get_xml(url['GET_ID'].format(userid, apikey))

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

    root = get_xml(url['GET_INFO'].format(matchid, apikey))
    stats = match_stat(root)

    return stats


def match_stat(root=None):
    """Get Dota 2 Last Match Statistics"""
    match = {'lastdota': {}}
    hero = 0

    try:
        match['lastdota']['match_id'] = root.find('match_id').text
        match['lastdota']['radiant_win'] = root.find('radiant_win').text
        match['lastdota']['start_time'] = datetime.fromtimestamp(int(root.find('start_time').text)).strftime('%d, %B %Y %H:%M:%S')
        match['lastdota']['duration'] = datetime.fromtimestamp(int(root.find('duration').text)).strftime('%M:%S')
        match['lastdota']['game_mode'] = root.find('game_mode').text
        match['lastdota']['cluster'] = root.find('cluster').text
        match['lastdota']['positive_votes'] = root.find('positive_votes').text
        match['lastdota']['negative_votes'] = root.find('negative_votes').text
    except:
        raise ParseError

    try:
        match['lastdota']['first_blood_time'] = datetime.fromtimestamp(int(root.find('first_blood_time').text)).strftime('%M:%S')
    except:
        pass

    hours = (match['lastdota']['duration'])[:-3]
    minutes = (match['lastdota']['duration'])[3:]
    match['lastdota']['goldtime'] = round(float(hours) + (float(minutes) / 60), 1)

    mode = dota2lib.mode
    a = int(match['lastdota']['game_mode'])
    if a in mode.keys():
        match['lastdota']['game_mode'] = mode[a]['name']
    else:
        pass

    cluster = dota2lib.cluster
    a = int(match['lastdota']['cluster'])
    if a in cluster.keys():
        match['lastdota']['cluster'] = cluster[a]['name']
    else:
        pass

    heroes = dota2lib.heroes
    items = dota2lib.items
    test = {}

    for a in root.findall('./players/player'):
        try:
            account_id = a.find('account_id').text
            if account_id == "4294967295":
                hero += 1
                account_id = str(hero)
            else:
                pass
            player_slot = a.find('player_slot').text
            hero_id = heroes[int(a.find('hero_id').text)]['name']
            avatar = heroes[int(a.find('hero_id').text)]['avatar']
            kills = a.find('kills').text
            deaths = a.find('deaths').text
            assists = a.find('assists').text
            gold_per_min = a.find('gold_per_min').text
            xp_per_min = a.find('xp_per_min').text
            last_hits = a.find('last_hits').text
            level = a.find('level').text
            item_0 = items[int(a.find('item_0').text)]['avatar']
            item_1 = items[int(a.find('item_1').text)]['avatar']
            item_2 = items[int(a.find('item_2').text)]['avatar']
            item_3 = items[int(a.find('item_3').text)]['avatar']
            item_4 = items[int(a.find('item_4').text)]['avatar']
            item_5 = items[int(a.find('item_5').text)]['avatar']

            match['lastdota'][account_id] = {"player_slot": player_slot,
                                              "heroid": hero_id,
                                              "avatar": avatar,
                                              "kills": kills,
                                              "deaths": deaths,
                                              "assists": assists,
                                              "gold_per_min": gold_per_min,
                                              "xp_per_min": xp_per_min,
                                              "last_hits": last_hits,
                                              "level": level,
                                              "item_0": item_0,
                                              "item_1": item_1,
                                              "item_2": item_2,
                                              "item_3": item_3,
                                              "item_4": item_4,
                                              "item_5": item_5}
        except:
            raise

    return match