#!/usr/bin/env python3
from flask import render_template, session, redirect, url_for, flash
from statsmile import app, db, STEAM_API_KEY, dota


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
    dota.GetDota(session['user_id'], STEAM_API_KEY)
    flash("Update complete!")
    return redirect(url_for('profile'))