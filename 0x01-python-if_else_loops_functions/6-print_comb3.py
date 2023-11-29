#!/usr/bin/python3

for i in range(10):
    sep = ", " if i != 8 or j != 9 else "\n"
    for j in range(i + 1, 10):
        print("{:d}{:d}{}".format(i, j, sep), end="")
