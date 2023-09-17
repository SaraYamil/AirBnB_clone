#!/usr/bin/python3

""" define the Amenity Module"""

from models.base_model import BaseModel


class Amenity(BaseModel):
"""Represent an amenity.
    Attributes:
        name (str): The name of the amenity.
    """

    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes an Amenity instance"""
        super().__init__(*args, **kwargs)
