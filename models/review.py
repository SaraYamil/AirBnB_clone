#!/usr/bin/python3

""" define the review Module"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class

    Attributes:
        place_id (str): id of Place
        user_id (str): id of user
        text (str): Review text

    Methods:
        __init__: Constructor of the Review class
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Initializes a Review instance"""
        super().__init__(*args, **kwargs)
