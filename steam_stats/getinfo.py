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
            b = a.find('hoursOnRecord').text
            c = a.find('name').text
            d = a.find('logo').text
            if ',' in b:
                b = b.replace(",", "")
                b = float(b)
                games[b] = [c, d]
            else:
                b = float(b)
                games[b] = [c, d]
        except:
            pass

    time = sum(games.keys())
    test = games.keys()
    best = sorted(games, reverse=True)[:5]
    best_time = sum(best)
    other_time = time - best_time

    post = {"games": {"time": time,
                      "count": count,
                      "other_time": other_time,
                      "best_time": best_time,
                      "best1": {"name": games[best[0]][0], "avatar": games[best[0]][1], "hours": best[0]},
                      "best2": {"name": games[best[1]][0], "avatar": games[best[1]][1], "hours": best[1]},
                      "best3": {"name": games[best[2]][0], "avatar": games[best[2]][1], "hours": best[2]},
                      "best4": {"name": games[best[3]][0], "avatar": games[best[3]][1], "hours": best[3]},
                      "best5": {"name": games[best[4]][0], "avatar": games[best[4]][1], "hours": best[4]}}}

    return post