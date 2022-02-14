#!/usr/bin/python3
"""
script that takes in a URL and an email address
sends a POST request to the passed URL with the email as a parameter
and finally displays the body of the response
"""

import requests
from sys import argv


def urlRequest(url, email):
    """ Function that sends a post request """
    values = {'email': email}

    r = requests.post(url, data=values)
    print(r.text)

if __name__ == "__main__":
    urlRequest(argv[1], argv[2])
