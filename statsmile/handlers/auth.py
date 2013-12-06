#!/usr/bin/env python3

from tornado import gen
from tornado.auth import OpenIdMixin
from tornado.escape import json_encode
from tornado.web import asynchronous, HTTPError

from statsmile.common import get_steam_user, getting_matches
from .base import BaseHandler


class AuthLoginHandler(BaseHandler, OpenIdMixin):

    _OPENID_ENDPOINT = "http://steamcommunity.com/openid/login"

    @asynchronous
    @gen.engine
    def get(self):
        if self.get_argument("openid.mode", None):
            self.get_authenticated_user(self.async_callback(self._on_auth))
            return
        self.authenticate_redirect()

    def _on_auth(self, user):

        if not user:
            raise HTTPError(500, "Steam Auth Failed")
        rv = self.application.db['users'].find_one({'steamid': user['claimed_id'][-17:]})

        temp = self.session_data()

        if not rv:
            userid = get_steam_user(self.application.db, user['claimed_id'][-17:])
            self.application.db['users'].insert(userid)
            temp['userid'] = userid['_id']
            self.application.db['sessions'].insert(temp)
            getting_matches(self.application.db, user['claimed_id'][-17:])
        else:
            temp['userid'] = rv['_id']
            self.application.db['sessions'].insert(temp)

        self.set_secure_cookie("st_usr", json_encode(str(temp['_id'])))
        self.redirect('/')


class AuthLogoutHandler(BaseHandler):
    def get(self):
        self.application.db['sessions'].remove({'_id': self.current_user})
        self.clear_cookie("st_usr")
        self.redirect('/')