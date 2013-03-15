import dota2parser
import dota2lib
import ConfigParser

config = ConfigParser.ConfigParser()
config.read('config.ini')

apikey = config.get('data', 'apikey')

def match_stats(userid=None):

	error = "Connection Error!"

	match = dota2parser.dota2match(userid, apikey)

	if match == "Connection Error!":

		return error

	else:

		pass

	match_details = dota2parser.details_match(match, apikey)
	match_hero = dota2parser.details_hero(match, apikey)

	lib = dota2lib.GameMode
	a = int(match_details['game_mode'])
	if a in lib.keys():
		match_details['game_mode'] = lib[a]['name']
		print match_details['game_mode']
	else:
		pass

	lib = dota2lib.Heroes

	for it in match_hero:

		a = int(match_hero[it]['hero_id'])
	
		if a in lib.keys():

			match_hero[it]['hero_id'] = lib[a]['name']
			match_hero[it]['avatar'] = lib[a]['avatar']

		else:

			pass

	lib = dota2lib.Items

	for it in match_hero:

		a = int(match_hero[it]['item_0'])
		
		if a in lib.keys():

			match_hero[it]['item_0'] = lib[a]['avatar']

		else:

			pass

	for it in match_hero:

		a = int(match_hero[it]['item_1'])

		if a in lib.keys():

			match_hero[it]['item_1'] = lib[a]['avatar']

		else:

			pass

	for it in match_hero:

		a = int(match_hero[it]['item_2'])

		if a in lib.keys():

			match_hero[it]['item_2'] = lib[a]['avatar']

		else:

			pass

	for it in match_hero:

		a = int(match_hero[it]['item_3'])

		if a in lib.keys():

			match_hero[it]['item_3'] = lib[a]['avatar']

		else:

			pass

	for it in match_hero:

		a = int(match_hero[it]['item_4'])

		if a in lib.keys():

			match_hero[it]['item_4'] = lib[a]['avatar']

		else:

			pass

	for it in match_hero:

		a = int(match_hero[it]['item_5'])

		if a in lib.keys():

			match_hero[it]['item_5'] = lib[a]['avatar']

		else:

			pass

	return match_details, match_hero