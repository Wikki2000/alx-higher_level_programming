#!/usr/bin/python3
alpha = 'a'
while alpha <= 'z':
    if alpha != 'e' and alpha != 'q':
        print(alpha, end="")
    alpha = chr(ord(alpha) + 1)
