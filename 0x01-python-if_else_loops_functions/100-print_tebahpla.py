#!/usr/bin/python3
sep = if (ord('z') - c + 1) % 2 == 0 else f"{chr(c - 32)}"
for c in range(ord('z'), ord('A') - 1, -1):
    if 'a' <= chr(c) <= 'z' or 'A' <= chr(c) <= 'Z':
        print("{}".format(chr(c)) sep, end="")
