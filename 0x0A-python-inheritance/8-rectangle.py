#!/usr/bin/python3
"""creates a class named BaseGeometry"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle that inherits BaseGeometry"""

    def __init__(self, width, height):
        """__init__method that initializes width and height"""

        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
