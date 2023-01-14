#!/usr/bin/python3
"""Unittest for max_integer([..])
Author:
    Abdulsalam Abdulsomad .A. - January 14th, 2023.
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    '''A class that tests a function for its biggest integer.'''

    def test_ordered(self):
        ''' Tests an ordered list.'''
        ordered = [1, 2, 3, 4, 5, 6]
        self.assertEqual(max_integer(ordered), 6)

    def test_scattered(self):
        ''' Tests a scattered list. '''
        scattered = [1, 7, 5, 3, 2, 4, 6]
        self.assertEqual(max_integer(scattered), 7)

    def test_single_arg(self):
        ''' Tests a list with only one item. '''
        single_arg = [14]
        self.assertEqual(max_integer(single_arg), 14)

    def test_empty_list(self):
        ''' Tests an empty list. '''
        empty_list = []
        self.assertIsNone(max_integer(empty_list))

    def test_begin_max(self):
        ''' Tests a list that begins with its max. '''
        begin_max = [8, 4, 7, 5]
        self.assertEqual(max_integer(begin_max), 8)

    def test_floats(self):
        ''' Tests if floats work correctly. '''
        floats = [1.2, 2.3, 3.0, 6.7]
        self.assertEqual(max_integer(floats), 6.7)

    def test_floats_n_ints(self):
        ''' Tests a lists containing ints and floats. '''
        floats_n_ints = [1.2, 3.4, -6, 7.8, 8.9, 10]
        self.assertEqual(max_integer(floats_n_ints), 10)

    def test_negative(self):
        ''' Tests a list whose items are all negative digits. '''
        negative = [-6, -5, -1]
        self.assertEqual(max_integer(negative), -1)

    if __name__ == "__main__":
        unittest.main()
