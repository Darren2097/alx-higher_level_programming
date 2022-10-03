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

        for i in range(self.y):
            print()
        for r in range(self.height):
            for j in range(self.x):
                print(' ', end='')
                for c in range(self.width):
                    print('#', end='')
                print()

    def __str__(self):
        """prints a string to stdout"""
        return ("[{}] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            type(self).__name__,
            self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""

        if len(args > 0):
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.width = arg
                if i == 2:
                    self.height = arg
                if i == 3:
                    self.x = arg
                if i == 4:
                    self.y = arg
        elif len(kwargs) > 0:
            for j, kwarg in kwargs.items():
                if j == 'id':
                    self.id = kwarg
                if j == 'width':
                    self.width = kwarg
                if j == 'height':
                    self.height = kwarg
                if j == 'x':
                    self.x = kwarg
                if j == 'y':
                    self.y = kwarg

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""

        obj_dict = {}

        for i, kwarg in self.__dict__.items():
            if i == 'id':
                obj_dict['id'] = kwarg
            if i == '_Rectangle__width':
                obj_dict['width'] = kwarg
            if i == '_Rectangle__height':
                obj_dict['height'] = kwarg
            if i == '_Rectangle__x':
                obj_dict['x'] = kwarg
            if i == '_Rectangle__y':
                obj_dict['y'] = kwarg

        return obj_dict
