#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    argc = len(argv) - 1
    if argc == 0:
        print("0 arguments.")
    else:
        print("{} argument:".format(argc))
        for i in range(1, argc + 1):
            print("{}: {}".format(i, argv[i]))
