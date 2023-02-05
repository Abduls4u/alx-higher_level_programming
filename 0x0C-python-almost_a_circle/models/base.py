#!/usr/bin/python3
''' A module cobtains an ancestor or Base class.
Usage:
    ./base.py
Author:
    Abdulsalam Abdulsomad .A. - February 4th, 2023.
'''
import json


class Base:
    '''Base class to all classes in this project. '''
    __nb_objects = 0

    def __init__(self, id=None):
        '''Constructs all the necessary attributes for the Base class. '''

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        '''returns json representation '''
        jstr = ''
        if list_dictionaries is None:
            jstr = '"[]"'
        else:
            jstr = json.dumps(list_dictionaries)
        return (jstr)
