#!/usr/bin/env python3

from bson.json_util import dumps, loads


def json_decode(value):
    return loads(value)


def json_encode(value):
    return dumps(value).replace("</", "<\\/")