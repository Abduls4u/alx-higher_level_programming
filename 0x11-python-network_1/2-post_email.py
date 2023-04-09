#!/usr/bin/python3
'''Sends a POST request to a url.
Usage:
   ./2-post_email.py <url> <mail>
Author:
    Abdulsalam Abdulsomad .A. - April 9th, 2023.
'''
import urllib.request as request
import urllib.parse as parse
import sys


if len(sys.argv) > 1:
    url = sys.argv[1]
    values = {'email': sys.argv[2]}
    data = parse.urlencode(values)
    data = data.encode('ascii')
    req = request.Request(url, data)
    with request.urlopen(req) as response:
        the_mail = response.read().decode()
        print(f'{the_mail}')
