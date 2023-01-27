#!/usr/bin/python3
''' Contains a function that deserializes a JSON string.
Usage:
    ./4-from_json_string.py
Author:
    Abdulsalam Abdulsomad .A. - January 27th, 2023.
'''
import json


def from_json_string(my_str):
    ''' A function that returns an object (Python data structure)
represented by a JSON string.
    Parameters:
    -----------
        my_str(str): JSON string to deserialize.
    Return(obj):
        The python representation of a JSON string.
    '''

    return (json.loads(my_str))
