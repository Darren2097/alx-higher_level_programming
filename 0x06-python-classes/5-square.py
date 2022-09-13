#!/usr/bin/python3
"""Creates a class named Square"""


class Square:
    """Square class"""

    def __init__(self, size=0):
        """Initializes a __init__ method that sets the size of a square"""

        self.size = size

    def area(self):
        """gets the area of the square"""

        return (self.__size * self.__size)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """sets the size of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def my_print(self):
        """prints in stdout the square with the character #"""

        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end='')
            print()

        if self.__size == 0:
            print()
