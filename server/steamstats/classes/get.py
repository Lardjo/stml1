#!/usr/bin/env python3
# classes\get.py

import requests
import xml.etree.ElementTree as ET


class GetUserStats:
    """
    Class Get User Stats
    Main class for get user statistics
    """
    def __init__(self, steamid, apikey):
        """
        Init function
        Default settings
        """
        self.steamid = steamid
        self.apikey = apikey
        self.match_id = None
        self.dict = {'steam': {}, 'games': {}, 'dota-game': {}}
        self.steam()
        self.dota()


    def steam(self):
        """
        Steam function
        Get all information about user
        """
        r = requests.get("http://steamcommunity.com/profiles/{0}?xml=1".format(self.steamid))
        root = ET.fromstring(r.text)
        for child in root:
            self.dict['steam'][child.tag] = child.text


    def dota(self):
        """
        Dota 2 function
        Get information about last match
        """
        options = {'matches_requested': '1', 'account_id': self.steamid, 'key': self.apikey} # Options
        r = requests.get("https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/", params=options)
        json = r.json() # convert to JSON
        self.match_id = json['result']['matches'][0]['match_id'] or None # Get ID Match
        options = {'match_id': self.match_id, 'key': self.apikey} # Set new options for request
        r = requests.get("https://api.steampowered.com/IDOTA2Match_570/GetMatchDetails/V001/", params=options)
        json = r.json()
        self.dict['dota-game'] = json['result']

if __name__ == "__main__":
    print("Ok! You just run this file. Don't import")
