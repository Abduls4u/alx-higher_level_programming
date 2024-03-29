#!/usr/bin/python3
'''Sends a request to a url
Usage:
   ./7-error_code.py <url>
Author:
    Abdulsalam Abdulsomad .A. - April 9th, 2023.
'''
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            req = requests.get(sys.argv[1])
            req.raise_for_status()
            print(f'{req.text}')
        except requests.HTTPError as error:
            code = int(error.response.status_code)
            if code >= 400:
                print(f'Error code: {code}')
