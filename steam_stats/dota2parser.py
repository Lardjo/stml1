import requests
import os
import xml.etree.ElementTree as ET
 
def details(match=None, apikey=None):

	tmp = 'tmp/'
	name = 'dota2details'
	dota2details = "https://api.steampowered.com/IDOTA2Match_570/GetMatchDetails/V001/?format=XML&match_id={0}&key={1}".format(match, apikey)

	file_name = os.path.join(tmp, name + ".xml")
	r = requests.get(dota2details)
	with open(file_name, "wb") as code:
		code.write(r.content)

	tree = ET.parse(file_name)
	root = tree.getroot()

	details_match = {}

	for a in root.findall('./players/player'):

		try:

			account_id = a.find('account_id').text
			player_slot = a.find('player_slot').text
			hero_id = a.find('hero_id').text
			details_match[account_id] = {'player_slot': player_slot, 'hero_id': hero_id}

		except:

			error = "Error!"
			return error

	return details_match


def dota2match(userid=None, apikey=None):

	tmp = 'tmp/'
	name = 'dota2match'
	dota2math = "https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/?format=XML&matches_requested=1&account_id={0}&key={1}".format(userid, apikey)

	file_name = os.path.join(tmp, name + ".xml")
	r = requests.get(dota2math)
	with open(file_name, "wb") as code:
		code.write(r.content)

	tree = ET.parse(file_name)
	root = tree.getroot()

	for a in root.findall('./matches/match'):

		try:

			match = a.find('match_id').text

		except:

			match = "none"

	return match