#!/usr/bin/python3
''' Contains a function that creates an object from a json file.
Usage:
    ./5-load_from_json_file.py
Author:
    Abdulsalam Abdulsomad .A. - January 27th, 2023.
'''
import json


def load_from_json_file(filename):
    ''' A function that creates an Object from a “JSON file”
    Parameters:
    -----------
        filename(str): Name of the file to write to.
    '''

    with open(filename) as myfile:
        return (json.load(myfile))
