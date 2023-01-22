#!/usr/bin/python3
''' A module that contains the class MyInt that inherits from int.
Usage:
    ./100-my_int.py
Author:
    Abdulsalam Abdulsomad .A. - January 22nd, 2023.
Assistance - @Betascribbles
'''


class MyInt(int):
    ''' A class that inverts == to != and vice versa'''

    def __ne__(self, value):
        """Override != operator with == behavior."""
        return self.real == value

    def __eq__(self, value):
        """Override == opeartor with != behavior."""
        return self.real != value
