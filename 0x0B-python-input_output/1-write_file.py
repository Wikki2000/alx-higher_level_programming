#!/usr/bin/python3

"""
======================
1-write_file.py module
======================
"""


def write_file(filename="", text=""):
    """Function to write and return number of written str"""
    with open(filename, 'w', encoding='UTF-8') as file:
        return file.write(text)
