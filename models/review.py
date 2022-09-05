#!/usr/bin/python3
"""
This module contains the Review class

Class:
    Review : define Review
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """class that define Review"""
    place_id = str("")
    user_id = str("")
    text = str("")
