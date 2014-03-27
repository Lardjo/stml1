#!/usr/bin/env python3

from datetime import datetime

from motor import Op
from tornado.auth import OpenIdMixin
from tornado.gen import engine, coroutine
from tornado.escape import json_encode
from tornado.web import asynchronous, HTTPError

from statsmile.common import get_user, json_code
from .base import BaseHandler


class AuthLoginHandler(BaseHandler, OpenIdMixin):
    """Auth Login Handler

    Main Authentication handler. Path: /auth/login
    """
    _OPENID_ENDPOINT = 'http://steamcommunity.com/openid/login'

    @asynchronous
    @coroutine
    def get(self):

        if self.get_argument('openid.mode', None):

            user = yield self.get_authenticated_user()

            if not user:
                raise HTTPError(500, 'Steam Auth Failed')

            rv = yield Op(self.db.users.find_one, {'claimed_id': user['claimed_id'][-17:]})
            sess = self.upd_session()

            if not rv:
                user = yield get_user(self.settings['api_key'], user['claimed_id'][-17:])
                self.db.users.insert(user)
                sess['user'] = user['_id']
                sess['signed_in'] = datetime.now()
                self.db.sessions.insert(sess)

            else:
                sess['user'] = rv['_id']
                sess['signed_in'] = datetime.now()
                self.db.sessions.insert(sess)

            self.set_secure_cookie('user_session', json_encode(str(sess['_id'])))
            self.redirect(self.get_argument('next', '/'))

        else:
            self.authenticate_redirect()


class AuthLogoutHandler(BaseHandler):
    """Auth Logout Handler

    Re-authentication Handler. Path: /auth/logout
    """
    def get(self):
        self.db.sessions.remove({'_id': self.current_user['_id']})
        self.clear_cookie('user_session')
        self.redirect(self.get_argument('next', '/'))


class AuthHandler(BaseHandler):

    def prepare(self):
        super().prepare()
        self.set_header('Content-Type', 'application/json; charset=UTF-8')

    @asynchronous
    @engine
    def get(self):
        if self.current_user:
            session = yield Op(self.db.users.find_one, {'_id': self.current_user['user_id']})
            self.write(json_code.json_encode({'auth': True, 'user': session}))
            self.finish()
            return
        self.write(json_code.json_encode({'auth': False, 'user': None}))
        self.finish()
        return