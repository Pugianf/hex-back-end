#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL
and displays the body of the response
"""

import requests
from sys import argv


def urlRequest(url):
    """Function that sends a request"""
    r = requests.get(url)
    code = r.status_code
    if code < 400:
        print(r.text)
    else:
        print('Error code: {}'.format(code))

if __name__ == '__main__':
    urlRequest(argv[1])
