#!/usr/bin/python3
'''
Usage:
    ./0-lookup.py
Author:
    Abdulsalam Abdulsomad .A. - January 20th, 2023.
'''


def lookup(obj):
    '''Returns the list of available attributes and methods of an object .'''

    attr = []
    attr.append(dir(obj))
    return (attr)
