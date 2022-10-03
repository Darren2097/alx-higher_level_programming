#!/usr/bin/python3
"""creates the class Square that inherits from Rectangle"""
from rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """__init__ method of square class"""

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """gets the size of square"""
        return self.width

    @size.setter
    def size(self, size):
        """sets the size of square"""

        if not isinstance(size, int):
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be > 0")

        self.width = size
        self.height = size

    def __str__(self):
        """prints a string to stdout"""

        return ("[{}] ({:d}) {:d}/{:d} - {:d}".format(
            type(self).__name__, self.id, self.x, self.y, self.width))

    def update(self, *args, **kwargs):
        """assigns attributes"""

        if len(args) > 0:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.size = arg
                if i == 2:
                    self.x = arg
                if i == 3:
                    self.y = arg
        elif len(kwargs) > 0:
            for j, kwarg in kwargs.items():
                if j == 'id':
                    self.id = kwarg
                if j == 'size':
                    self.size = kwarg
                if j == 'x':
                    self.x = kwarg
                if j == 'y':
                    self.y = kwarg

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""

        obj_dict = {}

        for i, kwarg in self.__dict__.items():
            if i == 'id':
                obj_dict['id'] = kwarg
            if i == 'size':
                obj_dict['_Square__size'] = kwarg
            if i == 'x':
                obj_dict['_Square__x'] = kwarg
            if i == 'y':
                obj_dict['_Square__y'] = kwarg

        return obj_dict
