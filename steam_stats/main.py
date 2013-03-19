# -*- coding: utf-8 -*-
# Welcome

import requests

from contextlib import closing
from flask import Flask, session, url_for, g, render_template, request, flash, redirect, _app_ctx_stack

# configuration
SECRET_KEY = "\x8bf\xb86c\xb0[\x93\xed\xce\x05!\x0ee\xbcr\xa3`-W\xb7\xf33\xab"

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

@app.route('/')
def main(name=None, total=None):

	if not session.get('logged_in'):
		return render_template('index.html')
	else:
		pass

	return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():

	if request.method == 'POST':

		session['logged_in'] = True
		session['username'] = request.form['username']

		return redirect(url_for('main'))

	return render_template('login.html')

@app.route('/logout')
def logout():

	session.pop('logged_in', None)
	return redirect(url_for('main'))

if __name__ == "__main__":
#	init_db()
	app.run(debug=True)