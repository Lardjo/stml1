# Get all info
# Steam Stats

import app
import dota2lib
import xml.etree.ElementTree as ET

from datetime import datetime

def SteamProfile(root=None):
	"""Steam Profile Info"""
	post = {}
	try:
		privacy = root.find('privacyState').text
		post['privacy'] = privacy
		steamid = root.find('steamID').text
		post['steamid'] = steamid
		steamid64 = root.find('steamID64').text
		post['steamid64'] = steamid64
		status = root.find('onlineState').text
		post['status'] = status
		membersince = root.find('memberSince').text
		post['membersince'] = membersince
		avatar = root.find('avatarFull').text
		post['avatar'] = avatar
	except:
		pass
	try:
		location = root.find('location').text
		post['location'] = location
	except:
		pass
	try:
		rating = root.find('steamRating').text
		post['rating'] = rating
	except:
		pass
	try:
		realname = root.find('realname').text
		post['realname'] = realname
	except:
		pass
	try:
		ingameinfo = root.find('./inGameInfo/gameName').text
		post['ingameinfo'] = ingameinfo
	except:
		pass
	try:
		hoursplayed = root.find('hoursPlayed2Wk').text
		post['hoursplayed'] = hoursplayed
	except:
		pass

	return post

def SteamGames(root=None):
	"""Steam Games Info"""
	games = {}
	count = 0
	for a in root.findall('./games/game'):
		count+=1
		try:
			b = a.find('hoursOnRecord').text
			c = a.find('name').text
			if ',' in b:
				b = b.replace(",", "")
				b = float(b)
				games[c] = b		
			else:
				b = float(b)
				games[c] = b
		except:
			b = 0

	HoursTotal = sum(games.values())
	DictTotal = sorted(games, key=games.get, reverse=True)[:5]
	ListHoursTotalGames = [games.get(DictTotal[0]), games.get(DictTotal[1]), games.get(DictTotal[2]), games.get(DictTotal[3]), games.get(DictTotal[4])]
	TotalHoursBest = sum(ListHoursTotalGames)
	OtherHours = HoursTotal - TotalHoursBest

	post = {"hourstotal": HoursTotal,
			"game1": DictTotal[0],
			"game2": DictTotal[1],
			"game3": DictTotal[2],
			"game4": DictTotal[3],
			"game5": DictTotal[4],
			"game1hours": games.get(DictTotal[0]),
			"game2hours": games.get(DictTotal[1]),
			"game3hours": games.get(DictTotal[2]),
			"game4hours": games.get(DictTotal[3]),
			"game5hours": games.get(DictTotal[4]),
			"otherhours": OtherHours,
			"totalgames": count}

	return post

def Matchid(root=None):
	"""Get Dota 2 Last Match id"""
	match = None
	try:
		status = root.find('status').text
		if status == "15":
			return 0
		else:
			pass
	except:
		pass
	for a in root.findall('./matches/match'):
		try:
			match = a.find('match_id').text
		except:
			pass

	return match

def MatchStat(root=None):
	"""Get Dota 2 Last Match Statistics"""
	match = {}
	try:
		match['match_id'] = root.find('match_id').text
		match['radiant_win'] = root.find('radiant_win').text
		match['start_time'] = datetime.fromtimestamp(int(root.find('start_time').text)).strftime('%d, %B %Y %H:%M:%S')
		match['duration'] = datetime.fromtimestamp(int(root.find('duration').text)).strftime('%M:%S')
		match['game_mode'] = root.find('game_mode').text
		match['cluster'] = root.find('cluster').text
		match['positive_votes'] = root.find('positive_votes').text
		match['negative_votes'] = root.find('negative_votes').text
	except:
		pass
	try:
		match['first_blood_time'] = datetime.fromtimestamp(int(root.find('first_blood_time').text)).strftime('%M:%S')
	except:
		pass

	hours = (match['duration'])[:-3]
	minuts = (match['duration'])[3:]
	match['goldtime'] = round(float(hours) + (float(minuts) / 60), 1)

	lib = dota2lib.GameMode
	a = int(match['game_mode'])
	if a in lib.keys():
		match['game_mode'] = lib[a]['name']
	else:
		pass
	lib = dota2lib.Cluster
	a = int(match['cluster'])
	if a in lib.keys():
		match['cluster'] = lib[a]['name']
	else:
		pass
	
	return match

def MatchInfo(root=None, steam32=None):
	"""Get Dota 2 Last Match Heroes"""
	match_details = {}
	hero = 0
	for a in root.findall('./players/player'):
		try:
			account_id = a.find('account_id').text
			if account_id == "4294967295":
				account_id = str(hero)
				hero+=1
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
			item_0 = a.find('item_0').text
			item_1 = a.find('item_1').text
			item_2 = a.find('item_2').text
			item_3 = a.find('item_3').text
			item_4 = a.find('item_4').text
			item_5 = a.find('item_5').text

			match_details[account_id] = {	"player_slot": player_slot,
											"hero_id": hero_id, 
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
			pass

	lib = dota2lib.Heroes
	for it in match_details:
		a = int(match_details[it]['hero_id'])
		if a in lib.keys():
			match_details[it]['hero_id'] = lib[a]['name']
			match_details[it]['avatar'] = lib[a]['avatar']
		else:
			pass

	lib = dota2lib.Items
	for it in match_details:
		a = int(match_details[it]['item_0'])
		if a in lib.keys():
			match_details[it]['item_0'] = lib[a]['avatar']
		else:
			pass

	for it in match_details:
		a = int(match_details[it]['item_1'])
		if a in lib.keys():
			match_details[it]['item_1'] = lib[a]['avatar']
		else:
			pass

	for it in match_details:
		a = int(match_details[it]['item_2'])
		if a in lib.keys():
			match_details[it]['item_2'] = lib[a]['avatar']
		else:
			pass

	for it in match_details:
		a = int(match_details[it]['item_3'])
		if a in lib.keys():
			match_details[it]['item_3'] = lib[a]['avatar']
		else:
			pass

	for it in match_details:
		a = int(match_details[it]['item_4'])
		if a in lib.keys():
			match_details[it]['item_4'] = lib[a]['avatar']
		else:
			pass

	for it in match_details:
		a = int(match_details[it]['item_5'])
		if a in lib.keys():
			match_details[it]['item_5'] = lib[a]['avatar']
		else:
			pass

	for a in match_details.keys():
		if steam32 == int(a):
			match_details[a]['you'] = '1'
		else:
			pass

	return match_details