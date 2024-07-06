#!/usr/bin/python3
"""
Sends a request to a given URL and displays the body of the response,
handling urllib.error.HTTPError exceptions.

Usage: ./3-error_code.py <URL>
"""
import sys
from urllib import request, error

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)
    except error.HTTPError as e:
        print(f"Error code: {e.code}")
