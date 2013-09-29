#!/usr/bin/env python3
import requests
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import ParseError


class GetUser:

    def __init__(self, steamid, steamkey):
        self.steamid = steamid
        self.steamkey = steamkey
        self.user = {"dt2mt": []}
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