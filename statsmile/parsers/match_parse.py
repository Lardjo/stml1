#!/usr/bin/env python3


def parse_match(match):
    """Parsing match information

    Function is to produce clearance dictionary and converts some of the elements
    """
    match['record_status'] = True

    if (match['human_players'] < 10) or (match['duration'] < 360):
        match['record_status'] = False

    # Clear match
    del match['tower_status_radiant']
    del match['tower_status_dire']
    del match['barracks_status_radiant']
    del match['barracks_status_dire']
    del match['leagueid']
    del match['positive_votes']
    del match['negative_votes']
    del match['human_players']

    for player in match['players']:

        # Put all items in the list
        player['items'] = [player['item_0'],
                           player['item_1'],
                           player['item_2'],
                           player['item_3'],
                           player['item_4'],
                           player['item_5']]

        # Clear all items
        del player['item_0']
        del player['item_1']
        del player['item_2']
        del player['item_3']
        del player['item_4']
        del player['item_5']

        del player['leaver_status']

        # Gold
        player['gold'] = int(round(player['gold_per_min'] * (match['duration'] / 60), 0))

        # Remove ability list
        try:
            del player['ability_upgrades']
        except KeyError:
            pass

        # Check account id
        try:
            if player['account_id'] == 4294967295:
                player['account_id'] = False
        except KeyError:
            player['account_id'] = False

        # Set team for better understanding
        if player['player_slot'] < 5:
            player['radiant_team'] = True
        else:
            player['radiant_team'] = False

        # Check valid hero_id
        if player['hero_id'] == 0:
            match['record_status'] = False

    return match