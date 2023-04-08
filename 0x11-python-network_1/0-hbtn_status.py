#!/usr/bin/python3
''' fetches a url.
Usage:
   ./0-hbtn_status.py
Author:
    Abdulsalam Abdulsomad .A. - April 8th, 2023.
'''
import urllib.request as request


with request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    status = response.read()
    print("Body response:")
    print(f'\t- type: {(type(status))}')
    print(f'\t- content: {status}')
    print(f'\t- utf8 content: {status.decode()}')
