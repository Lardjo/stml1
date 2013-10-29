#!/usr/bin/env python3
from bson import ObjectId
from .base import BaseHandler


class UserHandler(BaseHandler):
    """
    UserHandler
    Users individual pages
    """
    def get(self, sid=None):
        """
        Function Get
        Parameters: ../user/<sid>
        """
        user = self.application.db['users'].find_one({"steamid": sid})
        session = self.application.db['users'].find_one({"_id": ObjectId(self.current_user)})

        if user:
            self.render("profile.html", user=user, session=session)
        else:
            self.render("404.html", session=session)