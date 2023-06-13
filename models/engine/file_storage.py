#!/usr/bin/python3
"""File Storage"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    __file_path = 'file.json'
    __objects = {}
    class_dict = {"BaseModel": BaseModel, "User": User, "State": State,
                  "City": City, "Amenity": Amenity, "Place": Place,
                  "Review": Review}

    def all(self):
        return self.__objects

    def new(self, obj):
        if obj:
            key = '{}.{}'.format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        dct = {}
        for key, obj in self.__objects.items():
            dct[key] = obj.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(dct, f)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as f:
                new_obj = json.load(f)
            for key, value in new_obj.items():
                obj = self.class_dict[value['__class__']](**value)
                self.__objects[key] = obj
        except FileNotFoundError:
            pass
