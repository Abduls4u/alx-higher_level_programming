#!/usr/bin/python3
''' A module that inherits from Rectangle.
Usage:
    ./square.py
Author:
    Abdulsalam Abdulsomad .A. - February 4th, 2023.
'''
from models.rectangle import Rectangle


class Square(Rectangle):
    ''' A class that represents a square '''

    def __init__(self, size, x=0, y=0, id=None):
        '''Constructs all the necessary attributes for the square object.
        parameters:
        ___________
             size: length of one of the side of the square.
             x: x axis
             y: y axis
        '''

        super().__init__(size, size, x, y, id)

    def __str__(self):
        ''' returns informal representation '''
        sqr = f"[Square] ({self.id}) {self.x}/{self.y} - {self.height}"
        return (sqr)

    @property
    def size(self):
        '''Getter method to retrieve size '''
        return (self.width)

    @size.setter
    def size(self, value):
        '''setter method to set the value of size'''
        self.width = value
        self.height = value
