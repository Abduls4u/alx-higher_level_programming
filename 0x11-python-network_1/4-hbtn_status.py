#!/usr/bin/python3
'''fetches a url
Usage:
   ./4-hbtn_status.py
Author:
    Abdulsalam Abdulsomad .A. - April 9th, 2023.
'''
import requests


if __name__ == "__main__":
    status = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print(f'\t- type: {(type(status.text))}')
    print(f'\t- content: {status.text}')

