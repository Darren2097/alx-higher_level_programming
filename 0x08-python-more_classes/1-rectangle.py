#!/usr/bin/python3
"""Creates a class Rectangle that defines a rectangle"""


class Rectangle:
    """Rectangle class"""

    def __init__(self, width=0, height=0):
        """Initializes a __init__ method that sets the size of a rectangle"""

        self.width = width
        self.height = height

    @property
    def width(self):
        """returns width"""

        return self.__width

    @width.setter
    def width(self, value):
        """sets the width"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """returns height"""

        return self.__height

    @height.setter
    def height(self, value):
        """sets the height"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__height = value
