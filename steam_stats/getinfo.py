# Get all info
# Steam Stats

import xml.etree.ElementTree as ET

def SteamProfile(root=None):
	"""Steam Profile Info"""
	try:
		Privacy = root.find('privacyState').text
	except:
		Privacy = "none"
	try:
		SteamID = root.find('steamID').text
	except:
		SteamID = "none"
	try:
		SteamID64 = root.find('steamID64').text
	except:
		SteamID64 = "none"
	try:
		Status = root.find('onlineState').text
	except:
		Status = "none"
	try:
		Location = root.find('location').text
	except:
		Location = "none"
	try:
		Rating = root.find('steamRating').text
	except:
		Rating = "none"
	try:
		RealName = root.find('realname').text
	except:
		RealName = "none"
	try:
		memberSince = root.find('memberSince').text
	except:
		memberSince = "none"
	try:
		inGameInfo = root.find('./inGameInfo/gameName').text
	except:
		inGameInfo = "none"
	try:
		hoursPlayed = root.find('hoursPlayed2Wk').text
	except:
		hoursPlayed = "none"
	try:
		Avatar = root.find('avatarFull').text
		Avatar = ("src=" + Avatar) 
	except:
		Avatar = 'data-src=holder.js/64x64'


	post = {"steamid": SteamID, 
			 "steamid64": SteamID64, 
			 "status": Status, 
			 "location": Location, 
			 "rating": Rating, 
			 "realName": RealName, 
			 "avatar": Avatar, 
			 "privacy": Privacy, 
			 "membersince": memberSince, 
			 "ingameinfo": inGameInfo,
			 "hoursplayed": hoursPlayed}

	return 1

def SteamGames(root=None):
	"""Steam Games Info"""

	Dict = {}
	i = 0

	for a in root.findall('./games/game'):

		i+=1

		try:

			b = a.find('hoursOnRecord').text
			c = a.find('name').text

			if ',' in b:

				b = b.replace(",", "")
				b = float(b)
				Dict[c] = b
				
			else:

				b = float(b)
				Dict[c] = b

		except:

			b = 0

	HoursTotal = sum(Dict.values())
	DictTotal = sorted(Dict, key=Dict.get, reverse=True)[:6]
	ListHoursTotalGames = [Dict.get(DictTotal[0]), Dict.get(DictTotal[1]), Dict.get(DictTotal[2]), Dict.get(DictTotal[3]), Dict.get(DictTotal[4]), Dict.get(DictTotal[5])]
	TotalHoursBest = sum(ListHoursTotalGames)
	OtherHours = HoursTotal - TotalHoursBest

	post = {"hourstotal": HoursTotal,
			"game1": DictTotal[0],
			"game2": DictTotal[1],
			"game3": DictTotal[2],
			"game4": DictTotal[3],
			"game5": DictTotal[4],
			"game1hours": Dict.get(DictTotal[0]),
			"game2hours": Dict.get(DictTotal[1]),
			"game3hours": Dict.get(DictTotal[2]),
			"game4hours": Dict.get(DictTotal[3]),
			"game5hours": Dict.get(DictTotal[4]),
			"otherhours": OtherHours,
			"totalgames": i}

	return 1