# -*- coding: utf-8 -*-
# Welcome

import sqlite3
import os
import re
import requests
import xml.etree.ElementTree as ET

from contextlib import closing
from flask import Flask, session, url_for, g, render_template, request, redirect, _app_ctx_stack

# configuration
TMP = 'tmp/'
DATABASE = 'data.db'
DEBUG = True
SECRET_KEY = "\x8bf\xb86c\xb0[\x93\xed\xce\x05!\x0ee\xbcr\xa3`-W\xb7\xf33\xab"

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

#def init_db():
#	with app.app_context():
#		db = get_db()
#		with app.open_resource('schema.sql') as f:
#			db.cursor().executescript(f.read())
#		db.commit()

def get_db():
	top = _app_ctx_stack.top
	if not hasattr(top, 'db'):
		db = sqlite3.connect(app.config['DATABASE'])
		db.row_factory = sqlite3.Row
		top.db = db

	return top.db

@app.teardown_appcontext
def close_db_connection(exception):
	top = _app_ctx_stack.top
	if hasattr(top, 'db'):
		top.db.close()

@app.route('/')
def main(name=None, total=None):

	db = get_db()
	cur = db.execute('select id, login from entries order by id desc limit 8')
	entries = cur.fetchall()

	if not session.get('logged_in'):

		return render_template('index.html', entries=entries)

	else:

		name = session['username']
		nameg = session['username']
		name = statistics(name)
		total = statgames(nameg)

	return render_template('index.html', entries=entries, name=name, total=total)

@app.route('/login', methods=['GET', 'POST'])
def login():

	if request.method == 'POST':

		session['logged_in'] = True
		session['username'] = request.form['username']

		db = get_db()
		db.execute('insert into entries (id, login) values (?, ?)', [None, request.form['username']])
		db.commit()

		return redirect(url_for('main'))

	return render_template('login.html')

@app.route('/logout')
def logout():

	session.pop('logged_in', None)
	return redirect(url_for('main'))


def statistics(name):

	STEAMXML = "http://steamcommunity.com/id/{0}?xml=1".format(name)

	file_name = os.path.join(TMP, name + ".xml")
	r = requests.get(STEAMXML)
	with open(file_name, "wb") as code:
		code.write(r.content)

	tree = ET.parse(file_name)
	root = tree.getroot()

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

	stats = [dict(SteamID = SteamID, 
					SteamID64 = SteamID64,	
					Status = Status, 
					Location = Location, 
					Rating = Rating,	
					RealName = RealName,
					Avatar = Avatar,
					Privacy = Privacy, 
					memberSince=memberSince,  
					inGameInfo=inGameInfo)]

	return stats

def statgames(nameg):

	STEAMXMLGAMES = "http://steamcommunity.com/id/{0}/games?xml=1".format(nameg)

	gfile_name = os.path.join(TMP, nameg + "_games.xml")
	gr = requests.get(STEAMXMLGAMES)
	with open(gfile_name, "wb") as code:
		code.write(gr.content)

	gtree = ET.parse(gfile_name)
	groot = gtree.getroot()

	Dict = {}
	#z = ","

	for a in groot.findall('./games/game'):

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
	#DictTotal = map(lambda x: re.sub("'|`", "", x), DictTotal)
	#print(DictTotal)

	ListHoursTotalGames = [Dict.get(DictTotal[0]), Dict.get(DictTotal[1]), Dict.get(DictTotal[2]), Dict.get(DictTotal[3]), Dict.get(DictTotal[4]), Dict.get(DictTotal[5])]
	TotalHoursBest = sum(ListHoursTotalGames)
	OtherHours = HoursTotal - TotalHoursBest

	gamestats = [dict(
		HoursTotal=HoursTotal,
		BestGame1=DictTotal[0],
		BestGame2=DictTotal[1],
		BestGame3=DictTotal[2],
		BestGame4=DictTotal[3],
		BestGame5=DictTotal[4],
		BestGame6=DictTotal[5],
		BestGame1Hours=Dict.get(DictTotal[0]),
		BestGame2Hours=Dict.get(DictTotal[1]),
		BestGame3Hours=Dict.get(DictTotal[2]),
		BestGame4Hours=Dict.get(DictTotal[3]),
		BestGame5Hours=Dict.get(DictTotal[4]),
		BestGame6Hours=Dict.get(DictTotal[5]),
		OtherHours=OtherHours
		)]

	return gamestats

if __name__ == "__main__":
#	init_db()
	app.run()