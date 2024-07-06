#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status using requests."""
import requests

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'


    # Send get request.
    response = requests.get(url)
    
    # Format the output as specified
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))
