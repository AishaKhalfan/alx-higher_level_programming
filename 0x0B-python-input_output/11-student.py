#!/usr/bin/python3
# 11-student.py
"""Defines a class Student"""


class Student:
    """Represents a student"""
    def __init__(self, first_name, last_name, age):
        """initializes a new student
        Args:
            first_name (str): The first name of the student
            last_name (str): The last name of the student
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the Student."""
        if (type(attrs) == list and
                all(type(elements) == str for elements in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance
        self.first_name = json['first_name']
        self.last_name = json['last_name']
        self.age = json['age']
        """
        for k, v in json.items():
            setattr(self, k, v)
