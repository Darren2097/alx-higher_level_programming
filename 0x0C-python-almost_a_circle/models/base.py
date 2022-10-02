#!/usr/bin/python3
"""Creates a class named Base. This class will be the base of the
other classes"""


class Base:
    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """__init__ method for base class"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
