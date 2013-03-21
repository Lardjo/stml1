# Get all info
# Steam Stats

import app
import pymongo
import xml.etree.ElementTree as ET

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

	posts = app.db
	post_id = posts.insert(post)

	return 1

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

	return 1