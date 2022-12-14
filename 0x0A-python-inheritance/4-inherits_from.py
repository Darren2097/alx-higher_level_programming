#!/usr/bin/python3
"""function that returns True if the object is an instance of a class
that inherited (directly or indirectly) from the specified
class; otherwise False"""


def inherits_from(obj, a_class):
    """inherits_from method"""

    if issubclass(type(obj), a_class):
        if type(obj) is not a_class:
            return True
    return False
