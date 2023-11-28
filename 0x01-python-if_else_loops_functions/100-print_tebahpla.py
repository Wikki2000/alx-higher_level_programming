#!/usr/bin/python3

for c in range(ord('z'), ord('A') - 1, -1):
    if 'a' <= chr(c) <= 'z' or 'A' <= chr(c) <= 'Z':
        print(f"{chr(c)}" if (ord('z') - c) % 2 == 0 else f"{chr(c - 32)}", end="")

