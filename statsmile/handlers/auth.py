#!/usr/bin/env python3
import tornado.auth
import tornado.escape
import tornado.web

from tornado import gen
from datetime import datetime
from .base import BaseHandler
from statsmile.data import get_steam_user


class AuthHandler(BaseHandler, tornado.auth.OpenIdMixin):
    """
    Steam Open ID auth. Hi, Gabe!
    """
    _OPENID_ENDPOINT = "http://steamcommunity.com/openid/login"

    @tornado.web.asynchronous
    @gen.coroutine
    def get(self):
        """
        Auth, cookie
        """
        if self.get_argument("openid.mode", None):
            claimed_id = yield self.get_authenticated_user()
            steamid = claimed_id["claimed_id"][-17:]
            rv = self.application.db["users"].find_one({"steamid": steamid})
            if not rv:
                user = get_steam_user(steamid)
                user["registration"] = datetime.now()
                self.application.db["users"].insert(user)
                self.set_secure_cookie("statsmile_user", tornado.escape.json_encode(str(user["_id"])))
                self.redirect("/")
            else:
                self.set_secure_cookie("statsmile_user", tornado.escape.json_encode(str(rv["_id"])))
                self.redirect("/")
            return
        else:
            yield self.authenticate_redirect()