#!/usr/bin/python3
''' sends a POST request to a url.
Usage:
   ./2-post_email.py
Author:
    Abdulsalam Abdulsomad .A. - April 9th, 2023.
'''
import urllib.request as request
import urllib.parse as parse
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = sys.argv[1]
        values = {'mail': sys.argv[2]}
        data = parse.urlencode(values)
        data = data.encode('ascii')
        req = request.Request(url, data)
        with request.urlopen(req) as response:
            the_mail = response.read()
            print(f'Your email is: {the_mail[0].decode()}')
