#!/usr/bin/python3
"""Base Module
Contains all the Base class which will be the
"base" of other classes in this project
"""
import json


class Base:
    """This class will be the “base” of all other classes in this project.
    The goal is to manage id attribute in all our future classes
    and to avoid duplicating the same code and same errors.
    Attributes:
        __nb_objects (int): the number of created Base objects.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the default attributes of the Base object.
        Args:
            id (int): the identifier of the Base object.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON representation of a string object."""
        if list_dictionaries is None or len(list_dictionaries) < 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to afile.
        Args:
            list_objs (list): a list of objects.
        """
        lst = []
        if list_objs is not None and len(list_objs) > 0:
            for obj in list_objs:
                lst.append(obj.to_dictionary())
        with open(cls.__name__ + ".json", 'w') as f:
            f.write(Base.to_json_string(lst))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string
        Args:
            json_dtring (str): a string representing a list of dict
        """
        if json_string is None and  len(json_string) < 0:
            return list()
        return json.loads(json_string)
