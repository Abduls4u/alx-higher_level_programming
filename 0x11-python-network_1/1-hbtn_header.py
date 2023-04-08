#!/usr/bin/python3
''' fetches the value of a header.
Usage:
   ./1-hbtn_header.py
Author:
    Abdulsalam Abdulsomad .A. - April 8th, 2023.
'''
import urllib.request as request
import sys


with request.urlopen(sys.argv[1]) as response:
    my_header_value = response.getheader('X-Request-Id')
    print(my_header_value)
