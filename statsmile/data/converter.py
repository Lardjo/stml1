#!/usr/bin/env python3


def converter(steam64):
    """
    Converter Steam ID 64 to 32
    All rights reserved. 2013. Konstantin N.
    """
    steam32 = int(steam64) - 76561197960265728
    return steam32

if __name__ == "__main__":
    value = int(input("Please, enter your Steam ID 64: "))
    print("Your Steam ID 32:", converter(value))