#!/usr/bin/python3
"""
Class User that inherits from BaseModel
"""

import json
from models.base_model import BaseModel


class User(BaseModel):
    """User Class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
