#!/usr/bin/python3
"""
Module Class City
"""
from models.base_model import BaseModel


class City(BaseModel):
    """ Inherits from BaseModel
    state_id will be State.id
    """
    state_id = ""
    name = ""
