#!/usr/bin/python3
# classes\api.py

import requests
import tornado.auth
import tornado.escape
import tornado.web

from tornado import gen
from datetime import datetime
from bson import ObjectId
from server.steamstats import config
from .get import GetUserStats

class BaseHandler(tornado.web.RequestHandler):
    """
    Class BaseHandler
    inc. get_current_user, session, prepare
    """
    def get_current_user(self):
        """
        Get Current User Function
        If user not auth, return None
        """
        user_json = self.get_secure_cookie("stats_user")
        if not user_json:
            return None
        return tornado.escape.json_decode(user_json)

    def session_now(self):
        """
        Session Function
        Update user information
        """
        data = {"last_login": datetime.now()}
        return data

    def prepare(self):
        """
        Prepare Function
        Check user cookies
        """
        token = self.get_current_user()
        if ObjectId.is_valid(token):
            if self.application.db['sessions'].find_one({"_id": ObjectId(token)}):
                self.application.db['sessions'].update({"_id": ObjectId(token)}, {"$set": self.session_now()})


class MainHandler(BaseHandler):
    """MainHandler"""
    def get(self):
        if self.get_current_user():
            self.render("index.html", title="Statemile",
                        session=self.application.db['sessions'].find_one({"_id": ObjectId(self.current_user)}))
        else:
            self.render("login.html", title="Statemile", session=None)


class AuthHandler(BaseHandler, tornado.auth.OpenIdMixin):
    """
    Class AuthHandler
    inc. get, _steam_user functions
    This is Steam Open ID auth
    """
    _OPENID_ENDPOINT = "http://steamcommunity.com/openid/login"

    @tornado.web.asynchronous
    @gen.coroutine
    def get(self):
        """
        Get Function
        Auth and set cookie
        """
        if self.get_argument("openid.mode", None):
            claimed_id = yield self.get_authenticated_user()
            self.steam_id = claimed_id["claimed_id"][-17:]
            rv = self.application.db['sessions'].find_one({"steamid": self.steam_id})
            if not rv:
                user = GetUserStats(self.steam_id, config.API_KEY).info()
                user["last_login"] = datetime.now()
                self.application.db['sessions'].insert(user)
                self.set_secure_cookie("stats_user", tornado.escape.json_encode(str(user['_id'])))
                self.redirect("/")
            else:
                self.set_secure_cookie("stats_user", tornado.escape.json_encode(str(rv['_id'])))
                self.redirect("/")
            return
        self.authenticate_redirect()


class LogoutHandler(BaseHandler):
    """
    Class LogoutHandler
    Logout and clear cookie
    """
    def get(self):
        self.clear_cookie("stats_user")
        self.redirect("/")
        return


class AboutHandler(BaseHandler):
    """
    Class AboutHandler
    Render about page
    """
    def get(self):
        self.render("about.html", title="Statemile",
                    session=self.application.db['sessions'].find_one({"_id": ObjectId(self.current_user)}))


class UserHandler(BaseHandler):
    """
    Class UserHandler
    Render users individual pages
    """
    def get(self, sid=None):
        """
        Function Get
        Parameters: ../user/<sid>
        """
        user = self.application.db['sessions'].find_one({"steamid": sid})
        if user:
            self.write("Hello, " + user['personaname'])
            self.write("\nYou real name is " + user['realname'])
            self.write("\nYou Steam profile url: " + user['profileurl'])
        else:
            self.write("User not found")