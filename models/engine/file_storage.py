#!/usr/bin/python3

import json
from models.base_model import BaseModel

class FileStorage:
    __file_path = 'file.json'
    __objects = {}
    class_dict = {"BaseModel": BaseModel}

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
