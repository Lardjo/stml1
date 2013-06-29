#!/usr/bin/env python3
from flask import render_template, session
from statsmile import app, db


@app.route('/')
def index():
    user = None
    if 'user_id' in session:
        user = db.posts.find_one({"steamid": session['user_id']})
    return render_template('index.html', user=user)


@app.route('/profile')
def profile():
    user = None
    if 'user_id' in session:
        user = db.posts.find_one({"steamid": session['user_id']})
    return render_template('profile.html', user=user)