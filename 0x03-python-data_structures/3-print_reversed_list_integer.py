#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    n = len(my_list) - 1
    if my_list is not None:
        while n >= 0:
            print("{:d}".format(my_list[n]))
            n -= 1
