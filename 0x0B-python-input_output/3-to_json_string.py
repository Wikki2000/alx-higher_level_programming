#!/usr/bin/python3

"""
==========================
3-to_json_string.py module
==========================
"""


from json import dumps


def to_json_string(my_obj):
    json_string = dumps(my_obj)
    return json_string
