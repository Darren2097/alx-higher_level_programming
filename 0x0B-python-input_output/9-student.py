#!/usr/bin/python3
"""Creates a class Student that defines a student"""


class_to_json = __import__('8-class_to_json').class_to_json


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """__init__ method that initializes a students first and
        last name and age"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a Student instance"""
        return class_to_json(self)
