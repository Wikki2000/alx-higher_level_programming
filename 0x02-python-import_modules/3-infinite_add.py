#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    if len(argv) == 1:
        print(0)
    else:
        new = list(map(int, argv[1:]))  # Exclude the script name
        print(sum(new))
