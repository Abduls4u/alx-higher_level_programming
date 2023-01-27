#!/usr/bin/python3
''' Contains a function that writes to a JSON file.
Usage:
    ./5-save_to_json_file.py
Author:
    Abdulsalam Abdulsomad .A. - January 27th, 2023.
'''
import json


def save_to_json_file(my_obj, filename):
    ''' A function that writes an Object to a text file, using a
JSON representation:
    Parameters:
    -----------
        my_obj: object to write to the text file in JSON format.
        filename: Name of the file to be written to.
    '''

    with open(filename, 'w', encoding='utf-8') as myfile:
        jrep = json.dumps(my_obj)
        myfile.write(jrep)
