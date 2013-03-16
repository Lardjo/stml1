Steam Stats [![Build Status](https://travis-ci.org/Lardjo/Steam-stats.png?branch=develop)](https://travis-ci.org/Lardjo/Steam-stats)
===========
Version: 1.1.0  
User statistics for Steam™. Experimental version. Used [Flask](https://github.com/mitsuhiko/flask) and [Bootstrap](https://github.com/twitter/bootstrap) Framework

## Quick start

System Requirements: Python 2.7.3, Flask 0.9  
Also used the library [HTTP Requests for Humans™](https://github.com/kennethreitz/requests)

* Download the latest release
* Run `main.py` from `./steam_stats`
* Go to the address `127.0.0.1:5000` in your browser

## Dota 2 Library

Starting with version 1.1.0 adds support for Dota 2. Display statistics for last match.  
You can use the library for their needs, but do not forget about the creator.  
File `dota2lib.py` from `./steam_stats` contains all heroes, clusters and game mode.  
Support items is not implemented in full (for version 0.9).