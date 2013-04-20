import requests
import tornado.auth
import tornado.escape
import tornado.web

from tornado import gen
from server.steamstats import config


class BaseHandler(tornado.web.RequestHandler):
    """BaseHandler"""
    def get_current_user(self):
        user_json = self.get_secure_cookie("stats_user")
        if not user_json:
            return None
        return tornado.escape.json_decode(user_json)


class MainHandler(BaseHandler):
    """MainHandler"""
    def get(self):
        if self.get_current_user():
            self.render("index.html", title="Steam Stats", session=self.current_user)
        else:
            self.render("login.html", title="Login")


class AuthHandler(BaseHandler, tornado.auth.OpenIdMixin):
    """Authenticate on Steam"""
    _OPENID_ENDPOINT = "http://steamcommunity.com/openid/login"

    @tornado.web.asynchronous
    @gen.coroutine
    def get(self):
        if self.get_argument("openid.mode", None):
            claimed_id = yield self.get_authenticated_user()
            self.steam_id = claimed_id["claimed_id"][-17:]
            user = self._steam_user()
            self.set_secure_cookie("stats_user", tornado.escape.json_encode(user))
            self.redirect("/")
            return
        self.authenticate_redirect()

    def _steam_user(self):
        """Get user information
        Just Steam Open ID sucks..."""
        options = {"key": config.API_KEY, "steamids": self.steam_id}
        r = requests.get("http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/", params=options)
        jsnobj = r.json()
        return jsnobj["response"]["players"][0] or {}


class LogoutHandler(BaseHandler):
    def get(self):
        self.clear_cookie("stats_user")
        self.redirect("/")
        return