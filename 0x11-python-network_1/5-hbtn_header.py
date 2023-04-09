#!/usr/bin/python3
''' fetches the value of a header.
Usage:
   ./5-hbtn_header.py
Author:
    Abdulsalam Abdulsomad .A. - April 8th, 2023.
'''
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        request = requests.get(sys.argv[1])
        print(request.headers.get('X-Request-Id'))
