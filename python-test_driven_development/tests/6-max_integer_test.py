#!/usr/bin/python3
"""
doc
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    doc
    """
    def test_max_int(self):
        """
        do list like [1,2,3,4,5,6,7] in assending, descending
        negative and random order work?
        """
        self.assertEqual(max_integer([1, 2, 3, 4, 5, 6, 6]), 6)
        self.assertEqual(max_integer([6, 6, 5, 4, 3, 2, 1]), 6)
        self.assertEqual(max_integer([1, 3, 2, 4, 6, 5]), 6)
        self.assertEqual(max_integer([-7, -6, -5, -4]), -4)

    def test_max_mixed_type(self):
        """
        does it for list of mixed type?
        """
        my_list = [2, 7, 6.0, 1.87]
        self.assertEqual(max_integer(my_list), 7)

    def test_max_str(self):
        """
        do list of strings works
        """
        my_list = ['yes', 'no']
        self.assertEqual(max_integer(my_list), "yes")

    def test_max_none(self):
        """
        does it return None for empty list?
        """
        self.assertIsNone(max_integer([]))

    def test_max_not_list(self):
        """
        does it raise an error for non list?
        """
        self.assertRaises((TypeError, ValueError), max_integer, 5)

    def test_max_single_el(self):
        """
        does a list of sigle element works
        """
        my_list = [6]
        self.assertEqual(max_integer(my_list), 6)

    if __name__ == "__main__":
        unittest.main()
