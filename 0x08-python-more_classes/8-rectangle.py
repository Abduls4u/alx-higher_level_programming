#!/usr/bin/python3
''' class that defines a rectangle.
Usage:
    ./8-rectangle.py
Author:
    Abdulsalam Abdulsomad .A. - January 2nd, 2023.
'''


class Rectangle:
    ''' A class that represents a square.'''

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        '''Constructs all the necessary attributes for the rectangle object.
        parameters:
        ___________
             width: Breadth of the rectangle.
             height: Length of the rectangle.
        '''

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        '''Getter method to retrieve width.'''
        return (self.__width)

    @width.setter
    def width(self, value):
        '''setter method to set the value of width.'''
        if not type(value) is int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''Getter method to retrieve the heght.'''
        return(self.__height)

    @height.setter
    def height(self, value):
        '''setter method to set value of height.'''
        if not type(value) is int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        ''' returns the area of a rectangle.
        parameters:
        __________
        Return:
            width X height.
        '''
        return (self.__width * self.__height)

    def perimeter(self):
        ''' returns the perimeter of a rectangle.
        parameters:
        __________
        Return:
            2(width + height).
        '''
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return (2 * (self.__width + self.__height))

    def __str__(self) -> str:
        '''prints the rectangle in an informal and printablr representation'''
        if self.__width == 0 or self.__height == 0:
            return ("")
        rectangle = ""
        for length in range(self.__height):
            for breadth in range(self.__width):
                try:
                    rectangle += str(self.print_symbol)
                except Exception:
                    rectangle += type(self).print_symbol
            if length < (self.__height - 1):
                rectangle += "\n"
        return (rectangle)

    def __repr__(self):
        '''prints the official represenatation of the rectangle.'''
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        '''prints a message when an instance is deleted'''
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
