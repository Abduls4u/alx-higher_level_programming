#!/usr/bin/python3
'''Sends a POST request to a url with a letter as parameter
Usage:
   ./6-post_email.py <url> <mail>
Author:
    Abdulsalam Abdulsomad .A. - April 9th, 2023.
'''
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) >= 1:
        letter = sys.argv[1]
    else:
        letter = ""
    values = {'q': letter}
    url = "http://0.0.0.0:5000/search_user"
    post_req = requests.post(url, values)
    json = post_req.json()
    try:
        if json == {}:
            print('No result')
        else:
            print(f"[{json.get('id')}] {json.get('name')}")
    except ValueError:
        print('Not a valid JSON')
