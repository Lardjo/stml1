#!/usr/bin/env python3


def parse_match(match):
    """Parsing match information

    Function is to produce clearance dictionary and converts some of the elements
    """

    if (match['human_players'] < 10) or (match['duration'] < 360):
        match['unregistered'] = True

    del match['tower_status_radiant']
    del match['tower_status_dire']
    del match['barracks_status_radiant']
    del match['barracks_status_dire']
    del match['leagueid']
    del match['positive_votes']
    del match['negative_votes']
    del match['human_players']

    for player in match['players']:

        player['items'] = [player['item_0'],
                           player['item_1'],
                           player['item_2'],
                           player['item_3'],
                           player['item_4'],
                           player['item_5']]

        del player['item_0']
        del player['item_1']
        del player['item_2']
        del player['item_3']
        del player['item_4']
        del player['item_5']

        del player['leaver_status']

        # Gold
        player['gold'] = int(round(player['gold_per_min'] * (match['duration'] / 60), 0))

        try:
            del player['ability_upgrades']
        except KeyError:
            pass

        try:
            if player['account_id'] == 4294967295:
                player['account_id'] = None
        except KeyError:
            player['account_id'] = None

        if player['player_slot'] < 5:
            player['radiant'] = True
        else:
            pass

        if player.get('hero_id', 0) == 0:
            match['unregistered'] = True

    return match