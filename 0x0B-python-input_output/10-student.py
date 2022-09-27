#!/usr/bin/python3
"""Creates a class Student that defines a student"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """__init__ method that initializes a students first and
        last name and age"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""

        obj_dict = self.__dict__

        if not attrs:
            return obj_dict
        else:
            filter_dict = {}
            for attr in attrs:
                if hasattr(self, attr):
                    filter_dict[attr] = obj_dict[attr]

            return filter_dict
