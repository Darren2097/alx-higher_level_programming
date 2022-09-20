#!/usr/bin/python3
"""Creates a class Rectangle that defines a rectangle"""


class Rectangle:
    """Rectangle class"""

    def __init__(self, width=0, height=0):
        """gets the width and height of rectangle"""

        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):

        if not isinstance(width, type):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")

        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        
        if not isinstance(height, type):
            raise TypeError("width must be an integer")
        if height < 0:
            raise ValueError("width must be >= 0")

        self.__height = height
