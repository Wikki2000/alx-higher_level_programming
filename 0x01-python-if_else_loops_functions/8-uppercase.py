#!/usr/bin/python3
def uppercase(str):
    for char in str:
        # Check if the character is a lowercase letter
        if 'a' <= char <= 'z':
            upper_char = chr(ord(char) - ord('a') + ord('A'))
        # Keep the character unchanged if it's not a lowercase letter
        else:
            upper_char = char
        print("{}".format(upper_char), end="")
    print()
