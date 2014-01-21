#!/usr/bin/env python3
import markdown
import re
import unicodedata

from tornado.gen import engine
from tornado.web import asynchronous, authenticated, UIModule, HTTPError
from motor import Op
from bson import ObjectId
from .base import BaseHandler
from datetime import datetime


class BlogHandler(BaseHandler):
    @asynchronous
    @engine
    def get(self):
        session = yield Op(self.db['users'].find_one, {'_id': self.current_user.get('userid', None)})
        cursor = self.db['blog'].find({}, sort=[('published', -1)], limit=10)
        entries = yield Op(cursor.to_list)
        if not entries:
            self.redirect('/blog/compose')
            return
        self.render("blog.html", entries=entries, session=session)


class EntryHandler(BaseHandler):
    @asynchronous
    @engine
    def get(self, slug):
        session = yield Op(self.db['users'].find_one, {'_id': self.current_user.get('userid', None)})
        entry = yield Op(self.db['blog'].find_one, {'slug': slug})
        author = yield Op(self.db['users'].find_one, {'_id': entry['author_id']})
        if not entry:
            raise HTTPError(404)
        self.render('entry.html', entry=entry, session=session, author=author)


class ComposeHandler(BaseHandler):
    @asynchronous
    @authenticated
    @engine
    def get(self):
        session = yield Op(self.db['users'].find_one, {'_id': self.current_user.get('userid', None)})
        id = self.get_argument('id', None)
        entry = None
        if id:
            entry = yield Op(self.db['blog'].find_one, {'_id': ObjectId(id)})
        self.render('compose.html', entry=entry, session=session)

    @asynchronous
    @authenticated
    @engine
    def post(self):
        id = self.get_argument('id', None)
        title = self.get_argument('title')
        text = self.get_argument('markdown')
        html = markdown.markdown(text)
        if id:
            entry = yield Op(self.db['blog'].find_one, {'_id': ObjectId(id)})
            if not entry:
                raise HTTPError(404)
            slug = entry['slug']
            self.db['blog'].update({'_id': ObjectId(id)}, {'$set': {'title': title,
                                                                    'html': html,
                                                                    'markdown': text}})
        else:
            slug = unicodedata.normalize('NFKD', title)
            slug = re.sub(r'[^\w]+', ' ', slug)
            slug = "-".join(slug.lower().strip().split())
            if not slug:
                slug = 'entry'
            e = yield Op(self.db['blog'].find_one, {'slug': slug})
            if not e:
                pass
            else:
                slug += "-2"

            self.db['blog'].insert({'author_id': self.current_user['userid'],
                                    'published': datetime.now(),
                                    'title': title,
                                    'slug': slug,
                                    'markdown': text,
                                    'html': html})
        self.redirect("/blog/entry/" + slug)


class EntryModule(UIModule):
    def render(self, entry):
        return self.render_string("modules/entry.html", entry=entry)