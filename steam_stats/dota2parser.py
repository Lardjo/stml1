import requests
import os
import datetime
import xml.etree.ElementTree as ET

def details_match(match=None, apikey=None):

	tmp = 'tmp/'
	name = 'dota2details_match'
	error = "Connection Error!"
	dota2details = "https://api.steampowered.com/IDOTA2Match_570/GetMatchDetails/V001/?format=XML&match_id={0}&key={1}".format(match, apikey)

	file_name = os.path.join(tmp, name + ".xml")
	r = requests.get(dota2details)
	with open(file_name, "wb") as code:
		code.write(r.content)

	tree = ET.parse(file_name)
	root = tree.getroot()

	details_match = {}

	try:

		details_match['match_id'] = root.find('match_id').text
		radiant_win = root.find('radiant_win').text
		time = root.find('start_time').text
		duration = root.find('duration').text

	except:

		error = "Error!"
		return error

	if radiant_win == "true":

		details_match['win'] = 'Radiant Victory!'

	else:

		details_match['win'] = 'Dire Victory!'
		
	time = datetime.datetime.fromtimestamp(int(time)).strftime('%d, %B %Y %H:%M:%S')
	duration = datetime.datetime.fromtimestamp(int(duration)).strftime('%M:%S')
	details_match['start_time'] = time
	details_match['duration'] = duration

	return details_match
 
def details_hero(match=None, apikey=None):

	tmp = 'tmp/'
	name = 'dota2details_hero'
	error = "Connection Error!"
	dota2hero = "https://api.steampowered.com/IDOTA2Match_570/GetMatchDetails/V001/?format=XML&match_id={0}&key={1}".format(match, apikey)

	file_name = os.path.join(tmp, name + ".xml")
	r = requests.get(dota2hero)
	with open(file_name, "wb") as code:
		code.write(r.content)

	tree = ET.parse(file_name)
	root = tree.getroot()

	details_hero = {}
	
	i = 0

	for a in root.findall('./players/player'):

		try:

			account_id = a.find('account_id').text

			if account_id == "4294967295":

				account_id = str(i)
				i+=1

			else:
				pass

			player_slot = a.find('player_slot').text
			hero_id = a.find('hero_id').text
			kills = a.find('kills').text
			deaths = a.find('deaths').text
			assists = a.find('assists').text
			gold_per_min = a.find('gold_per_min').text
			xp_per_min = a.find('xp_per_min').text
			last_hits = a.find('last_hits').text
			level = a.find('level').text
			details_hero[account_id] = {'player_slot': player_slot, 
			'hero_id': hero_id, 'kills': kills, 'deaths': deaths, 'assists': assists, 
			'gold_per_min': gold_per_min, 'xp_per_min': xp_per_min, 'last_hits': last_hits, 'level': level}

		except:

			error = "Error!"
			return error

	return details_hero


def dota2match(userid=None, apikey=None):

	tmp = 'tmp/'
	name = 'dota2match'
	error = "Connection Error!"
	dota2math = "https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/?format=XML&matches_requested=1&account_id={0}&key={1}".format(userid, apikey)
	file_name = os.path.join(tmp, name + ".xml")
	

	r = requests.get(dota2math)
	
	if r.status_code in (404, 500):

		return error

	else:

		pass
		
	with open(file_name, "wb") as code:
		code.write(r.content)


	tree = ET.parse(file_name)
	root = tree.getroot()

	match = "none"

	for a in root.findall('./matches/match'):

		try:

			match = a.find('match_id').text

		except:

			match = "none"

	return match