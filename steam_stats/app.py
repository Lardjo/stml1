import requests
import re
import ConfigParser

from flask import Flask, render_template, g, session, flash, redirect
from flask_openid import OpenID
from pymongo import MongoClient

# setup flask
app = Flask(__name__)
app.config.update(
    SECRET_KEY='development key',
    DEBUG=True
)

# config
config = ConfigParser.ConfigParser()
config.read('bin/config.ini')
STEAM_API_KEY = config.get('data', 'apikey')

# setup openid
oid = OpenID(app)

# mongodb
connection = MongoClient()
db = connection.stats_base

# other
_steam_id_re = re.compile('steamcommunity.com/openid/id/(.*?)$')
url = {"profile": "http://steamcommunity.com/id/{0}?xml=1",
       "games": "http://steamcommunity.com/id/{0}/games?xml=1",
       "matchid": "https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/?format=XML&matches_requested=1&account_id={0}&key={1}",
       "matchinfo": "https://api.steampowered.com/IDOTA2Match_570/GetMatchDetails/V001/?format=XML&match_id={0}&key={1}"}


def get_steam_userinfo(steam_id):
    """Get JSON file"""
    options = {'key': STEAM_API_KEY, 'steamids': steam_id}
    r = requests.get("http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/", params=options)
    jsnobj = r.json()
    return jsnobj['response']['players'][0] or {}


@app.before_request
def before_request():
    """Before request"""
    g.user = None
    if 'user_id' in session:
        g.user = session['user_id']


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
    """Create or login"""
    match = _steam_id_re.search(resp.identity_url)
    rv = db.posts.find_one({"steamid": match.group(1)})
    if rv is None:
        steamdata = get_steam_userinfo(match.group(1))
        rv = {"steamid": match.group(1), "nickname": steamdata['personaname']}
        db.posts.insert(rv)
    g.user = rv
    session['user_id'] = g.user
    flash('You are logged in as %s' % g.user['nickname'])
    return redirect(oid.get_next_url())


@app.route('/logout')
def logout():
    """Logout function"""
    session.pop('user_id', None)
    return redirect(oid.get_next_url())

if __name__ == "__main__":
    app.run()