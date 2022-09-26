#!/usr/bin/python3
"""function that returns True if the object is exactly an instance of the
specified class ; otherwise False"""


def is_same_class(obj, a_class):
    """is_same_class method"""

    if type(obj).__name__ == a_class.__name__:
        return True
    else:
        return False
