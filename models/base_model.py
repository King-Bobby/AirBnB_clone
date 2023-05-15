#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime

"""
Module base_model contains Class BaseModel
"""


class BaseModel:
    """
    Base class that contains methods:
        __init__(self, *args, **kwargs)
        __str__(self)
        save(self)
        to_dict(self)
    """
    def __init__(self, *args, **kwargs):
        """
        Initialises the class and class attributes id,
        created_at and updated_at
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Prints: [<class name>] (<self.id>) <self.__dict__>"""
        return (f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}')

    def save(self):
        """updates attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values
        of __dict__ of the instance"""
        dct = {}
        dct["__class__"] = self.__class__.__name__
        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                dct[key] = value.isoformat()
            else:
                dct[key] = value
        return dct
