#!/usr/bin/env python3

from .base import BaseHandler
from bson import ObjectId
from tornado.escape import url_escape
from tornado.httpclient import HTTPClient, HTTPError


class MainHandler(BaseHandler):
    def get(self):
        settings = self.application.db['settings'].find_one({"apikey": {"$exists": 'true'}})
        if settings is None:
            try:
                errormessage = self.get_argument("error")
            except:
                errormessage = ""
            self.render("get.html", errormessage=errormessage)
        else:
            if self.get_current_user():
                self.render("index.html",
                            session=self.application.db["users"].find_one({"_id": ObjectId(self.current_user)}))
            else:
                self.render("index.html", session=None)

    def check_apikey(self, apikey):
        url = "https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/?key={}".format(apikey)

        http_client = HTTPClient()
        try:
            http_client.fetch(url)
        except HTTPError as e:
            self.application.logger.error("Error: {}".format(e))
            return False

        http_client.close()
        self.application.logger.info("API key is valid. Ok")
        return True

    def post(self):
        apikey = self.get_argument('apikey', '')
        auth = self.check_apikey(apikey)
        if auth:
            settings = {"apikey": self.get_argument("apikey")}
            self.application.db["settings"].insert(settings)
            self.redirect("/")
        else:
            error_msg = "?error=" + url_escape("Your API key a invalid or Steam servers not available. "
                                               "Please, enter again")
            self.redirect("/" + error_msg)