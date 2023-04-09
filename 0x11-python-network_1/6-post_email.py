#!/usr/bin/python3
'''Sends a POST request to a url with a mail as parameter
Usage:
   ./6-post_email.py <url> <mail>
Author:
    Abdulsalam Abdulsomad .A. - April 9th, 2023.
'''
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        values = {'email': sys.argv[2]}
        url = sys.argv[1]
        post_req = requests.post(url, values)
        print(f'{post_req.text}')
