# -*- coding: utf-8 -*-
# Welcome

import ConfigParser
import requests
import pymongo
import getinfo
import getxml
import geturl

from contextlib import closing
from pymongo import MongoClient
from flask import Flask, session, url_for, g, render_template, request, flash, redirect, _app_ctx_stack

# configuration
SECRET_KEY = "\x8bf\xb86c\xb0[\x93\xed\xce\x05!\x0ee\xbcr\xa3`-W\xb7\xf33\xab"
MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017

config = ConfigParser.ConfigParser()
config.read('config.ini')
apikey = config.get('data', 'apikey')
nullid = int(config.get('data', 'identifier'))

# create application
app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

#def init_db():
#	"""Clear database"""
#	connection = MongoClient()
#	connection.drop_database("stats_base")

# connect to the database
def get_db():
    """Opens a new database connection"""
    connection = MongoClient()
    db = connection.stats_base
    return db

@app.route('/')
def main():
	"""Flask load"""
	if not session.get('logged_in'):
		return render_template('index.html')
	else:

		info = getinfo.SteamProfile(getxml.Download(geturl.url['profile'].format(session['username'])))
		steam32 = int(info['steamid64']) - nullid
		matchid = getinfo.Matchid(getxml.Download(geturl.url['matchid'].format(info['steamid64'], apikey)))
		info.update(getinfo.SteamGames(getxml.Download(geturl.url['games'].format(session['username']))))
		info.update(getinfo.MatchStat(getxml.Download(geturl.url['matchinfo'].format(matchid, apikey))))
		info.update(getinfo.MatchInfo(getxml.Download(geturl.url['matchinfo'].format(matchid, apikey)), steam32))

		db = get_db()
		posts = db.posts
		posts.insert(info)

	return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
	"""Login function"""
	if request.method == 'POST':

		session['logged_in'] = True
		session['username'] = request.form['username']

		return redirect(url_for('main'))

	return render_template('login.html')

@app.route('/logout')
def logout():
	"""Logout function"""
	session.pop('logged_in', None)
	return redirect(url_for('main'))

if __name__ == "__main__":
	app.run(debug=True)