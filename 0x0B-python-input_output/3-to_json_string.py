#!/usr/bin/python3
''' Contains a function that converts an object to JSON format.
Usage:
    ./3-to_json_string.py
Author:
    Abdulsalam Abdulsomad .A. - January 27th, 2023.
'''
import json


def to_json_string(my_obj):
    ''' A function that returns the JSON representation of an obj
ect (string)
    Parameters:
    -----------
        my_obj: object to convert to JSOM format.
    Return(str):
        The JSON representation of an object.
    '''

    return (json.dumps(my_obj))
