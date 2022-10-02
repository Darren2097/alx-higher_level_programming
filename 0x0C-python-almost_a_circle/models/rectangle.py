#!/usr/bin/python3
"""Creates a class named Rectangle that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """__init__ method for Rectangle class"""

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Rectangle width"""
        return self.__width

    @width.setter
    def width(self, width):
        """Sets rectangle width"""

        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """Rectangle height"""
        return self.__height

    @height.setter
    def height(self, height):
        """Sets rectangle height"""

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """Rectangle x"""
        return self.__x

    @x.setter
    def x(self, x):
        """Sets rectangle x-coordinate"""
        
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """Rectangle y"""
        return self.__y

    @y.setter
    def y(self, y):
        """sets rectangle y-coordinate"""

        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """gets the area of the rectangle"""
        return self.width * self.height

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""

        for r in range(self.height):
            for c in range(self.width):
                print('#', end='')
            print()

    def __str__(self):
        """prints a string to stdout"""
        return ("[{}] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            type(self).__name__, 
            self.id, self.x, self.y, self.width, self.height)
