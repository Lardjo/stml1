#!/usr/bin/env python3

from .base import BaseHandler
from bson import ObjectId


class MainHandler(BaseHandler):

    def get(self):
        exists = self.application.db['server'].find_one({'key': 'apikey'})
        if exists is None:
            self.render('index.html', title="Statsmile / Run Server", active="home", ready=False)
        else:
            session = self.application.db['sessions'].find_one({'_id': ObjectId(self.current_user)})
            if session:
                session = self.application.db['users'].find_one({'_id': session['userid']})
            self.render('index.html', title="Statsmile", active="home", ready=True, session=session)

    def post(self):
        settings = {'key': 'apikey', 'value': self.get_argument('apikey', '')}
        self.application.db['server'].insert(settings)
        self.redirect('/')