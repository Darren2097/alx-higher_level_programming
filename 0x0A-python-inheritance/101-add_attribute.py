#!/usr/bin/python3
"""function that adds a new attribute to an object if it’s possible"""

def add_new_attrib(obj, attr, value):
    """add_new_attrib method"""

    if hasattr(obj, "__dict__"):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")
