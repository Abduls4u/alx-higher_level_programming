#!/usr/bin/python3
'''Write a Python script that takes in a URL and an email, sends a
POST request to the passed URL with the email as a parameter, and 
displays the body of the response (decoded in utf-8)
The email must be sent in the email variable
You must use the packages urllib and sys
You are not allowed to import packages other than urllib and sys
You don’t need to check arguments passed to the script (number or type)
You must use the with statement
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
