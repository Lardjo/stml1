import requests
import re
import ConfigParser

from flask import Flask, render_template, g, session, flash, redirect, url_for
from flask_openid import OpenID
from pymongo import MongoClient

# setup app
config = ConfigParser.ConfigParser()
config.read('config.ini')

# setup flask
app = Flask(__name__)
app.config.update(
    SECRET_KEY = 'development key',
    DEBUG = True
)

# setup flask-openid
oid = OpenID(app)
_steam_id_re = re.compile('steamcommunity.com/openid/id/(.*?)$')

STEAM_API_KEY = config.get('data', 'apikey')

# connection
connection = MongoClient()
db = connection.stats_base\

def get_steam_userinfo(steam_id):
    """Get JSON file"""
    options = {'key': STEAM_API_KEY, 'steamids': steam_id}
    r = requests.get("http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/", params=options)
    jsnobj = r.json()
    return jsnobj['response']['players'][0] or {}

def get_or_create(steam_id):
    """Search in the base"""
    rv = db.posts.find_one({"steamid": steam_id})
    if rv is None:
        rv = db.posts.insert({"steamid": steam_id, "nickname": "None"})
    return rv

@app.before_request
def before_request():
    g.user = None
    g.name = None
    if 'user_id' in session:
        g.user = session['user_id']
        g.name = session['name']

@app.route('/')
def main():
    """Flask load"""
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
@oid.loginhandler
def login():
    """Login function"""
    if g.user:
        return redirect(oid.get_next_url())
    return oid.try_login('http://steamcommunity.com/openid')

@oid.after_login
def create_or_login(resp):
    match = _steam_id_re.search(resp.identity_url)
    g.user = get_or_create(match.group(1))
    steamdata = get_steam_userinfo(g.user["steamid"])
    g.user['nickname'] = steamdata['personaname']
    session['user_id'] = g.user['steamid']
    session['name'] = g.user['nickname']
    flash('You are logged in as %s' % g.user['nickname'])
    return redirect(oid.get_next_url())

@app.route('/logout')
def logout():
	"""Logout function"""
	session.pop('user_id', None)
	return redirect(oid.get_next_url())

if __name__ == "__main__":
	app.run()