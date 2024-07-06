#!/usr/bin/python3
"""Sends a POST request to a given URL with an email as a parameter,
and displays the body of the response (decoded in utf-8).

Usage: ./script.py <URL> <email>
"""
import sys
from urllib import request, parse

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # Create the data dictionary
    data = {'email': email}

    # Encode the data
    data = parse.urlencode(data).encode()

    # Create a Request object
    req = request.Request(url, data=data)

    # Send the request and display the response body
    with request.urlopen(req) as response:
        body = response.read().decode('utf-8')
        print(body)
