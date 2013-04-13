###
# Steam Stats (getinfo.py)
# https://github.com/Lardjo/Steam-stats
#
# Copyright 2013, Konstantin N.
# All right reserved
#
# Hi, Valve! Your Steam Web API SUCKS! FF, GGWP.
# Proxy API required for private-key API with public data, my ass. (c)
###

from getxml import download


class ParseError(Exception):
    pass


def user(user_id=None):
    """Steam Profile Info"""
    post = {'user_info': {}}
    url = "http://steamcommunity.com/profiles/{0}?xml=1".format(user_id)
    root = download(url)

    try:
        post['user_info']['privacy'] = root.find('privacyState').text
        post['user_info']['status'] = root.find('onlineState').text
        post['user_info']['membersince'] = root.find('memberSince').text
        post['user_info']['avatar'] = root.find('avatarFull').text
    except:
        raise ParseError

    try:
        post['user_info']['location'] = root.find('location').text
    except:
        pass

    try:
        post['user_info']['rating'] = root.find('steamRating').text
    except:
        pass

    try:
        post['user_info']['realname'] = root.find('realname').text
    except:
        pass

    try:
        post['user_info']['ingameinfo'] = root.find('./inGameInfo/gameName').text
    except:
        pass

    try:
        post['user_info']['hoursplayed'] = root.find('hoursPlayed2Wk').text
    except:
        pass

    url = "http://steamcommunity.com/profiles/{0}/games?xml=1".format(user_id)
    root = download(url)
    post.update(games(root))

    return post


def games(root=None):
    """Steam Games Info"""
    games = {}
    count = 0

    for a in root.findall('./games/game'):
        count += 1
        try:
            hours = a.find('hoursOnRecord').text
            name = a.find('name').text
            logo = a.find('logo').text
            appid = a.find('appID').text
            if ',' in hours:
                hours = hours.replace(",", "")
                games[appid] = {"name": name, "hours": float(hours), "logo": logo}
            else:
                games[appid] = {"name": name, "hours": float(hours), "logo": logo}
        except:
            pass

    time = reduce(lambda a, b: a + b, map(lambda x: x[1]['hours'], games.items()))
    dict_as_list = games.values()
    best = sorted(dict_as_list, key=lambda k: k['hours'], reverse=True)[:5]
    best_time = reduce(lambda a, b: a + b, map(lambda x: x['hours'], best))
    other_time = time - best_time

    post = {"games": {"time": time,
                      "count": count,
                      "other_time": other_time,
                      "best_time": best_time,
                      "best1": {"name": best[0]['name'], "avatar": best[0]['logo'], "hours": best[0]['hours']},
                      "best2": {"name": best[1]['name'], "avatar": best[1]['logo'], "hours": best[1]['hours']},
                      "best3": {"name": best[2]['name'], "avatar": best[2]['logo'], "hours": best[2]['hours']},
                      "best4": {"name": best[3]['name'], "avatar": best[3]['logo'], "hours": best[3]['hours']},
                      "best5": {"name": best[4]['name'], "avatar": best[4]['logo'], "hours": best[4]['hours']}}}

    return post