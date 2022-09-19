#!/usr/bin/python3
"""Module to find the max integer in a list
"""
import unittest


def max_integer(list=[]):
    """Function to find and return the max integer in a list of integers
    If the list is empty, the function returns None
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result

class TestMaxInteger(unittest.Testcase):

    def completeList(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([2, 5, 4, 9, 3]), 9)
        self.assertEqual(max_integer([-1, 3, 2, 5]), 5)

    def emptyList(self):
        self.assertEqual(max_integer([]), None)

if __name__ == '__main__':
    unittest.main()
