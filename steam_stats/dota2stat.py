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

	lib = dota2lib.Heroes

	for it in match_hero:

		a = int(match_hero[it]['hero_id'])
	
		if a in lib.keys():

			match_hero[it]['hero_id'] = lib[a]['name']
			match_hero[it]['avatar'] = lib[a]['avatar']

		else:

			pass

	return match_details, match_hero