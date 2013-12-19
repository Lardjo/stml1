#!/usr/bin/env python3

import motor

from random import choice
from string import ascii_letters, digits

from tornado.gen import coroutine
from pymongo.errors import DuplicateKeyError


class ParameterNotFound(Exception):
    pass


@coroutine
def get_cookies(db, key):

    try:
        db['server'].insert({"key": "cookie_secret",
                             "value": "".join([choice(ascii_letters + digits) for _ in range(30)])},
                            continue_on_error=True)
    except DuplicateKeyError:
        pass

    _ = yield motor.Op(db['server'].find_one, {'key': key})

    if _ is None:
        raise ParameterNotFound
    else:
        return _['value']