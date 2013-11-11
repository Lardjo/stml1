#!/usr/bin/env python3

import tornado.web
import tornado.auth

from tornado import gen
from tornado.escape import json_encode
from .base import BaseHandler
from statsmile.data import get_steam_user, getting_matches_id


class AuthHandler(BaseHandler, tornado.auth.OpenIdMixin):
    """
    Steam Open ID auth. Hi, Gabe!
    """
    _OPENID_ENDPOINT = "http://steamcommunity.com/openid/login"

    @tornado.web.asynchronous
    @gen.coroutine
    def get(self):
        if self.get_argument("openid.mode", None):
            claimed_id = yield self.get_authenticated_user()
            steamid = claimed_id["claimed_id"][-17:]
            rv = self.application.db["users"].find_one({"steamid": steamid})
            if not rv:
                user = get_steam_user(self.application.db, self.application.logger, steamid)
                self.application.db["users"].insert(user)
                self.set_secure_cookie("statsmile_user", json_encode(str(user["_id"])))
                self.redirect("/")
                yield getting_matches_id(self.application.db, self.application.logger, steamid)
            else:
                self.set_secure_cookie("statsmile_user", json_encode(str(rv["_id"])))
                self.redirect("/")
            return
        else:
            yield self.authenticate_redirect()