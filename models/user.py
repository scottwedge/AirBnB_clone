#!/usr/bin/python3
"""
class User that inherits from Base Model
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    User
    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''
