#!/usr/bin/python3
"""Creates a class named Base. This class will be the base of the
other classes"""
import json
import os.path
from os import path


class Base:
    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """__init__ method for base class"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""

        json_list = []
        json_str = '[]'

        if list_objs is not None:
            for obj in list_objs:
                json_list.append(obj.to_dictionary())

            if len(json_list) > 0:
                json_str = Base.to_json_string(json_list)

        with open(cls.__name__ + '.json', 'w') as f:
            f.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""

        if json_string is None or len(json_string) == 0:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""

        obj = None

        if cls.__name__ == 'Rectangle':
            obj = cls(1, 1)
        elif cls.__name__ == 'Square':
            obj = cls(1)

        cls.update(obj, **dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""

        obj_list = []

        try:
            with open(cls.__name__ + '.json', 'r', encoding='utf-8') as f:
                list_read = cls.from_json_string(f.read())
                for obj in list_read:
                    obj_list.append(cls.create(**obj))
        except Exception:
            pass

        return obj_list
