#!/usr/bin/python3
"""
This module contains the User class

Class:
    User : define User
"""

from models.base_model import BaseModel


class User(BaseModel):
    """class that define User"""
    email = str("")
    password = str("")
    first_name = str("")
    last_name = str("")
