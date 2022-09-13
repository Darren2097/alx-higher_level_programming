#!/usr/bin/python3
"""Creates and defines a class named Square"""


class Square:
    """Square class"""

    def __init__(self, size=0):
        """Initialize private instance attribute for square class"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
