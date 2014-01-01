#!/usr/bin/env python3

from tornado.gen import engine
from tornado.web import asynchronous, authenticated
from .base import BaseHandler
from motor import Op
from statsmile.common import libs


class BookmarksHandler(BaseHandler):
    @authenticated
    @asynchronous
    @engine
    def get(self):
        bookmarks = []
        session = None
        if self.current_user:
            session = yield Op(self.db['users'].find_one, {'_id': self.current_user['userid']})
        for mrks in session['bookmarks']:
            match = yield Op(self.db['matches'].find_one, {'match_id': mrks})
            bookmarks.append(match)
        self.render('bookmarks.html', title="Bookmarks", session=session, bookmarks=bookmarks,
                    mode=libs.mode, heroes=libs.heroes, cluster=libs.cluster)

    @authenticated
    def post(self):
        match = int(self.get_argument('match'))
        self.db['users'].update({'_id': self.current_user['userid']}, {'$pull': {'bookmarks': match} } )