#!/usr/bin/python3

"""
====================================
Module to save json string in a file
====================================
"""


from json import dump


def save_to_json_file(my_obj, filename):
    """Write json string to a file"""
    with open(filename, 'w', encoding='UTF-8') as file:
        dump(my_obj, file)
