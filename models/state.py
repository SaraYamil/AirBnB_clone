#!/usr/bin/python3

"""define state Module"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    represent state class

    Attributes:
        name (str): State name

    """
    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes a State instance"""
        super().__init__(*args, **kwargs)
