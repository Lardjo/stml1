#!/usr/bin/env python3

from random import choice
from string import ascii_letters, digits

from pymongo.errors import DuplicateKeyError


class ParameterNotFound(Exception):
    pass


def get_cookies(db, key):
    try:
        db['server'].insert({'key': 'cookie_secret',
                             'value': ''.join([choice(ascii_letters + digits) for _ in range(30)])},
                            continue_on_error=True)
    except DuplicateKeyError:
        pass

    _ = db['server'].find_one({'key': key})

    if _ is None:
        raise ParameterNotFound
    else:
        return _['value']