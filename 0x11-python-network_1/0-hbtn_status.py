#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status with a User-Agent."""
import urllib.request

if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    request = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(request) as response:
            body = response.read()
            print("Body response:")
            print("\t- type: {}".format(type(body)))
            print("\t- content: {}".format(body))
            print("\t- utf8 content: {}".format(body.decode("utf-8")))
    except urllib.error.HTTPError as e:
        print(f'HTTPError: {e.code} {e.reason}')
    except urllib.error.URLError as e:
        print(f'URLError: {e.reason}')
