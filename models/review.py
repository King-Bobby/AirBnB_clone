#!/usr/bin/python3
"""
Module class Review
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ inherits from BaseModel
    place_id will be Place.id
    user_id will be User.id
    """
    place_id = ""
    user_id = ""
    text = ""
