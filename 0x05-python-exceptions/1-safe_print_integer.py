#!/usr/bin/python3

def safe_print_integer(value):
    try:
        if isinstance(value, int) == 1:
            print("{:d}".format(value))
        return True
    except TypeError:
        return False
