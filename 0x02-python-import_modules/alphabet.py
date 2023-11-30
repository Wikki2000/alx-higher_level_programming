#!/usr/bin/python3

def print_alpha():
    alpha = 'A'
    while alpha <= 'Z':
        print("{}".format(alpha), end = ' ')
        alpha = chr(ord(alpha) + 1)
    print()
