import dota2parser
import dota2lib
import ConfigParser

#Radiant, Hero
player0 = "none"
player1 = "none"
player2 = "none"
player3 = "none"
player4 = "none"

#Dire, Hero
player128 = "none"
player129 = "none"
player130 = "none"
player131 = "none"
player132 = "none"

config = ConfigParser.ConfigParser()
config.read('config.ini')

apikey = config.get('data', 'apikey')

def match_stats(userid=None):

	match = dota2parser.dota2match(userid, apikey)
	match_details = dota2parser.details_match(match, apikey)
	match_hero = dota2parser.details_hero(match, apikey)

	lib = dota2lib.Heroes

	for it in match_hero:

		a = int(match_hero[it]['hero_id'])
	
		if a in lib.keys():

			match_hero[it]['hero_id'] = lib[a]['name']

		else:

			pass

	return match_details, match_hero

#print(match)
#print(match_details)
#print(match_hero)