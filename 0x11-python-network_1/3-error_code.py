#!/usr/bin/python3
'''Sends a POST request to a url with a mail as parameter
Usage:
   ./3-error_code.py <url>
Author:
    Abdulsalam Abdulsomad .A. - April 9th, 2023.
'''
import urllib.request as request
import urllib.error as error
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        req = request.Request(sys.argv[1])
        try:
            response = request.urlopen(req)
            print(f'{response.read().decode()}')
        except error.HTTPError as error:
            print(f'Error code: {error.code}')
