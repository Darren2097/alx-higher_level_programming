#!/usr/bin/python3
"""creates a class named BaseGeometry"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """raises an exception"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""

        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
