#!/usr/bin/python3
"""Sends a POST request to a given URL with an email as a parameter,
and displays the body of the response (decoded in utf-8).

Usage: ./script.py <URL> <email>
"""
import sys
from urllib import request, parse

if __name__ == "__main__":
    # Read command line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # Prepare data to be sent in the POST request
    data = parse.urlencode({'email': email}).encode()

    # Create a POST request
    req = request.Request(url, data=data, method='POST')

    # Send the request and handle the response
    with request.urlopen(req) as response:
        # Read and decode the response body
        body = response.read().decode('utf-8')
        print(body)
