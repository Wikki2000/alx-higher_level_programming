#!/usr/bin/python3

"""
======================
1-write_file.py module
======================
"""


def write_file(filename="", text=""):
        """Function to write a string to a text file
        and return the number of characters written.
        """
    with open(filename, 'w', encoding='UTF-8') as file:
        return file.write(text)
