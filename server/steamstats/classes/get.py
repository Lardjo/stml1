#!/usr/bin/python3
# classes\get.py

import requests

class GetUserStats:
    """
    Class Get User Stats
    Main class for get user statistics
    """
    def __init__(self, steamid, apikey):
        """
        Init function
        """
        self.steamid = steamid
        self.apikey = apikey


    def info(self):
        """
        info function
        """
        options = {"key": self.apikey, "steamids": self.steamid}
        r = requests.get("http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/", params=options)
        json_object = r.json()
        return json_object["response"]["players"][0] or {}