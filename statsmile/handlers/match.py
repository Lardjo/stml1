#!/usr/bin/env python3

from .base import BaseHandler

from statsmile.common import libs


class MatchHandler(BaseHandler):
    def get(self, match):
        session = self.application.db['sessions'].find_one({'_id': self.current_user})

        if session:
            session = self.application.db['users'].find_one({'_id': session['userid']})

        match = self.application.db["matches"].find_one({"match_id": int(match)})

        if match is None:
            return self.send_error(404)

        for (offset, item) in enumerate(match["players"]):

            if not "account_id" in item:
                match["players"][offset]["account_id"] = "Anonymous"
            else:
                player = self.application.db["users"].find_one({"steamid32": item["account_id"]})
                if player is None:
                    match["players"][offset]["account_id"] = "Anonymous"
                else:
                    match["players"][offset]["account_id"] = player["_id"]
                    match["players"][offset]["avatar"] = player["avatar"]
                    match["players"][offset]["personaname"] = player["personaname"]

        self.render("match.html", session=session, match=match, mode=libs.mode, cluster=libs.cluster,
                    heroes=libs.heroes, items=libs.items)