###
# Steam Stats
# https://github.com/Lardjo/Steam-stats
#
# Copyright 2013, Konstantin N.
# All right reserved
###

import requests
import re
import ConfigParser
import datetime

from flask import Flask, render_template, g, session, flash, redirect
from flask_openid import OpenID
from pymongo import MongoClient
from getinfo import user
from getdota import last_match


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


def get_steam_userinfo(steam_id):
    """Get JSON file"""
    options = {'key': STEAM_API_KEY, 'steamids': steam_id}
    r = requests.get("http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/", params=options)
    jsnobj = r.json()
    return jsnobj['response']['players'][0] or {}


def _jinja2_filter_datetime(date, fmt='%c'):
    # check whether the value is a datetime object
    if not isinstance(date, (datetime.date, datetime.datetime)):
        try:
            date = datetime.datetime.strptime(str(date), '%Y-%m-%d').date()
        except Exception, e:
            return date
    return date.strftime(fmt)

app.jinja_env.filters['datetime'] = _jinja2_filter_datetime


@app.before_request
def before_request():
    """Before request"""
    g.user = None
    if 'user_id' in session:
        g.user = session['user_id']


@app.route('/')
def main():
    """Flask load"""
    info = None
    if 'user_id' in session:
        info = db.posts.find_one({"steamid": session['user_id']})
    return render_template('stats-page.html', info=info)


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
        getinfo = user(match.group(1))
        getdota = last_match(match.group(1), STEAM_API_KEY)
        rv = {"steamid": match.group(1),
              "nickname": steamdata['personaname'],
              "profileurl": steamdata['profileurl'],
              "lastupdate": datetime.datetime.now()}
        rv.update(getinfo)
        rv.update(getdota)
        db.posts.insert(rv)
    g.user = rv
    session['user_id'] = g.user['steamid']
    flash('You are logged in as %s' % g.user['nickname'])
    return redirect(oid.get_next_url())


@app.route('/logout')
def logout():
    """Logout function"""
    session.pop('user_id', None)
    return redirect(oid.get_next_url())

if __name__ == "__main__":
    app.run()