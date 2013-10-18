import requests
from .api import apikey

def get_steam_user(steamid):
    """
    Get user information
    """
    options = {'key': apikey, 'steamids': steamid}
    r = requests.get("http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/", params=options)
    response = r.json()
    return response['response']['players'][0] or {}