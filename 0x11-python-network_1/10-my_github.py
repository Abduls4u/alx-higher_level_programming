#!/usr/bin/python3
'''Sends a POST request to a url with a letter as parameter
Usage:
   ./6-post_email.py <url> <mail>
Author:
    Abdulsalam Abdulsomad .A. - April 9th, 2023.
'''
import requests
from requests.auth import HTTPBasicAuth as auth
import sys


if __name__ == "__main__":
    verif = auth(sys.argv[1],sys.argv[2])
    req_json = requests.get("https://api.github.com/user", auth=verif).json()
    print(req_json.get('id'))
