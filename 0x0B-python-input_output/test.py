#!/usr/bin/python3

def class_to_json(obj):
    """return obj"""
    return vars(obj)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Creating an instance of the Person class
person_obj = Person('John', 30)

# Using class_to_json to get the dictionary representation of the object
json_representation = class_to_json(person_obj)

print(json_representation)

