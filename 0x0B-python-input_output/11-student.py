#!/usr/bin/python3
"""Creates a class Student that defines a student"""


def class_to_json(obj):
    """class_to_obj method"""

    return (obj.__dict__)


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

        obj_dict = class_to_json(self)

        if not attrs:
            return obj_dict
        else:
            filter_dict = {}
            for i, j in obj_dict.items():
                if i in attrs:
                    filter_dict[i] = j
            return filter_dict

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""

        for i, j in json.items():
            if hasattr(self, i):
                setattr(self, i, j)
