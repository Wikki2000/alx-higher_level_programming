#!/usr/bin/python3
"""Sends a POST request to a given URL with an email as a parameter,
and displays the body of the response (decoded in utf-8).

Usage: ./script.py <URL> <email>
"""
import sys
from urllib import request, parse

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./script.py <URL> <email>")
        sys.exit(1)

    # Read command line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # Prepare data to be sent in the POST request.
    # parse.urlencode converts it into a URL-encoded string.
    # encode() converts the URL-encoded string into bytes,
    # which is required for sending data in a POST request.
    data = parse.urlencode({'email': email}).encode()

    # Create a POST request object
    req = request.Request(url, data=data, method='POST')

    try:
        # Send the request and handle the response
        with request.urlopen(req) as response:
            # Read and decode the response body
            body = response.read().decode('utf-8')
        print("Email:", body)
    except Exception as e:
        print(f"Error: {e}")
