

def statistics(name):

	error = "Connection Error!"
	error_http = "No internet"

	STEAMXML = "http://steamcommunity.com/id/{0}?xml=1".format(name)

	file_name = os.path.join(TMP, name + ".xml")

	try:

		r = requests.get(STEAMXML)

	except requests.exceptions.ConnectionError:

		return error_http

	if r.status_code in (404, 500, 503):

		return error

	else:

		pass

	with open(file_name, "wb") as code:
		code.write(r.content)

	try:

		tree = ET.parse(file_name)
		root = tree.getroot()

	except:

		return error

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
		Avatar = root.find('avatarFull').text
		Avatar = ("src=" + Avatar) 
	except:
		Avatar = 'data-src=holder.js/64x64'

	try:
		hoursPlayed = root.find('hoursPlayed2Wk').text
	except:
		hoursPlayed = "none"

	stats = {'SteamID': SteamID, 
	'SteamID64': SteamID64, 
	'Status': Status, 
	'Location': Location, 
	'Rating': Rating, 
	'RealName': RealName, 
	'Avatar': Avatar, 
	'Privacy': Privacy, 
	'memberSince': memberSince, 
	'inGameInfo': inGameInfo,
	'hoursPlayed': hoursPlayed}

	return stats

def statgames(name=None):

	error = "Connection Error!"
	error_http = "No internet"

	STEAMXMLGAMES = "http://steamcommunity.com/id/{0}/games?xml=1".format(name)

	file_name = os.path.join(TMP, name + "_games.xml")

	try:

		r = requests.get(STEAMXMLGAMES)

	except requests.exceptions.ConnectionError:

		return error_http

	if r.status_code in (404, 500, 503):

		return error

	else:

		pass

	with open(file_name, "wb") as code:
		code.write(r.content)

	tree = ET.parse(file_name)
	root = tree.getroot()

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

	gamestats = {
		'HoursTotal': HoursTotal,
		'BestGame1': DictTotal[0],
		'BestGame2': DictTotal[1],
		'BestGame3': DictTotal[2],
		'BestGame4': DictTotal[3],
		'BestGame5': DictTotal[4],
		'BestGame6': DictTotal[5],
		'BestGame1Hours': Dict.get(DictTotal[0]),
		'BestGame2Hours': Dict.get(DictTotal[1]),
		'BestGame3Hours': Dict.get(DictTotal[2]),
		'BestGame4Hours': Dict.get(DictTotal[3]),
		'BestGame5Hours': Dict.get(DictTotal[4]),
		'BestGame6Hours': Dict.get(DictTotal[5]),
		'OtherHours': OtherHours,
		'totalgames': i
		}

	return gamestats