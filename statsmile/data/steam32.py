#!/usr/bin/env python3

STEAMNULL = 76561197960265728

def steamid(steam64):
    """
    Converter Steam ID 64 to 32
    All rights reserved. 2013. Konstantin N.
    """
    steam32 = int(steam64) - STEAMNULL
    return steam32