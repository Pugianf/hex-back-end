#!/usr/bin/python3
"""
Write a Python script that fetches https://intranet.hbtn.io/status
"""

import requests

""" Function that makes a request to a url."""
r = requests.get('https://intranet.hbtn.io/status')
print("Body response:")
print("\t- type: {}".format(type(r.text)))
print("\t- content: {}".format(r.text))
