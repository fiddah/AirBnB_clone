#!/usr/bin/python3
"""
This module contains the City class

Class:
    City : define City
"""

from models.base_model import BaseModel


class City(BaseModel):
    """class that define City"""
    state_id = str("")
    name = str("")
