#!/usr/bin/python3
"""Displays the X-Request-Id header variable of a request to a given URL.

Usage: ./1-hbtn_header.py <URL>
"""
import sys
from urllib import request


if __name__ == "__main__":
    url = sys.argv[1]

    # Create a request object
    req = request.Request(url)

    # Send the request and get the response
    with request.urlopen(req) as response:
        print(dict(response.headers).get("X-Request-Id"))
