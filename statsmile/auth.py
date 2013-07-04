#!/usr/bin/env python3
import requests
import re
import os
import configparser
import datetime

from flask import session, g, redirect, flash, url_for
from flask_openid import OpenID
from statsmile import app, db

# silence gold
config = configparser.ConfigParser()
config.read(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'core', 'core.ini'))
STEAM_API_KEY = config.get('data', 'apikey')

# openid
oid = OpenID(app)

# re
_steam_id_re = re.compile('steamcommunity.com/openid/id/(.*?)$')


def get_steam(steam_id):
    """ Get Steam JSON file """
    options = {'key': STEAM_API_KEY, 'steamids': steam_id}
    r = requests.get("http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/", params=options)
    user = r.json()
    return user['response']['players'][0] or {}


@app.before_request
def before_request():
    g.user = None
    if 'user_id' in session:
        g.user = session['user_id']


@app.route('/login', methods=['GET', 'POST'])
@oid.loginhandler
def login():
    if g.user:
        return redirect(oid.get_next_url())
    return oid.try_login('http://steamcommunity.com/openid')


@oid.after_login
def after_login(resp):
    match = _steam_id_re.search(resp.identity_url)
    rv = db.users.find_one({"steamid": match.group(1)})
    if rv is None:
        data = get_steam(match.group(1))
        rv = {"steamid": match.group(1),
              "nickname": data['personaname'],
              "realname": data['realname'],
              "avatar": data['avatarfull'],
              "url": data['profileurl'],
              "lastlogin": datetime.datetime.now()}
        db.users.insert(rv)
    g.user = rv
    session['user_id'] = g.user['steamid']
    flash('You are logged in as %s' % g.user['nickname'])
    return redirect(url_for('profile'))


@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('You are logout')
    return redirect(url_for('index'))