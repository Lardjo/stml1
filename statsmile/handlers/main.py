#!/usr/bin/env python3

from .base import BaseHandler


class MainHandler(BaseHandler):

    def get(self):
        exists = self.application.db['server'].find_one({'key': 'apikey'})
        if exists:
            if self.current_user:
                session = self.application.db['sessions'].find_one({'_id': self.current_user})
                user = self.application.db['users'].find_one({'_id': session['userid']})
                self.render("index.html", title="Statsmile", ready=True, user=user)
            self.render("index.html", title="Statsmile", ready=True)
        else:
            self.render("index.html", title="Statsmile / Run Server", ready=False)

    def post(self):
        settings = {'key': 'apikey', 'value': self.get_argument('apikey', '')}
        self.application.db["server"].insert(settings)
        self.redirect("/")