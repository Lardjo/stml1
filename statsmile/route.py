#!/usr/bin/env python3
from statsmile import app

@app.route('/')
def index():
    return 'Hello!'