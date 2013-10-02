#!/usr/bin/env python3
import requests
import xml.etree.ElementTree as ET

from xml.etree.ElementTree import ParseError
from datetime import datetime
from .steam32 import steam64to32

class GetUser:

    def __init__(self, steamid, steamkey):
        self.steamid = steamid
        self.steamkey = steamkey
        self.user = {}
        self.steam()

    def steam(self):
        r = requests.get("http://steamcommunity.com/profiles/{0}?xml=1".format(self.steamid))
        f = r.text
        root = ET.fromstring(f.encode('utf-8'))

        for child in root:
            try:
                self.user[child.tag] = child.text
            except ParseError:
                self.user[child.tag] = None

        self.user["steamID32"] = steam64to32(self.steamid)
        self.user["last_login"] = datetime.now()
        self.user["last_update"] = datetime.now()