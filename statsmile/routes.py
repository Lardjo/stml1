#!/usr/bin/env python3
from flask import render_template, session, redirect, url_for, flash
from statsmile import app, db, API_KEY, dota


@app.route('/')
def index():
    user = None
    if 'user_id' in session:
        user = db.users.find_one({"steamid": session['user_id']})
    return render_template('index.html', user=user)


@app.route('/profile')
def profile():
    if 'user_id' in session:
        user = db.users.find_one({"steamid": session['user_id']})
        return render_template('profile.html', user=user)
    return redirect(url_for('login'))


@app.route('/update')
def update():
    upd = dota.GetDota(session['user_id'], API_KEY).dota()
    if upd is None:
        flash("No new games for update. Come back later...")
    else:
        flash("Update complete! Add {0} new games.".format(upd))
    return redirect(url_for('profile'))