#!/usr/bin/python3

"""
==================
module 0-read_file
==================
"""


def read_file(filename=""):
    """Function to read file"""

    with open(filename, 'r', encoding='UTF-8') as file:
        content = file.read()
        print(content, end="")
