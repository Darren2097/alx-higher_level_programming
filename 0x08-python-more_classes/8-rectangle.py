#!/usr/bin/python3
"""Creates a class Rectangle that defines a rectangle"""


class Rectangle:
    """Rectangle class"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initializes a __init__ method that sets the size of a rectangle"""

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """returns the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """returns perimeter of rectangle"""

        if self.width == 0 or self.height == 0:
            return 0
        else:
            return ((2 * self.width) + (2 * self.height))

    def __str__(self):
        """prints the rectangle with the character #"""

        string = ''
        if self.width == 0 or self.height == 0:
            return string
        for i in range(self.height - 1):
            for j in range(self.width):
                string += str(self.print_symbol)
            string += '\n'
        string += str(self.print_symbol) * self.width
        return string

    def __repr__(self):
        """returns a string representation of the rectangle"""
        return ("Rectangle({:d}, {:d})".format(self.width, self.height))

    def __del__(self):
        """deletion method"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area"""

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() > rect_2.area():
            return rect_1
        elif rect1.area() == rect2.area():
            return rect_1
        else:
            return rect_2
