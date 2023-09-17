#!/usr/bin/python3

"""define User class module"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    User class

    Attributes:
        email (str): users email address
        password (str): users password
        first_name (str): user first name
        last_name (str): user last name

    Methods:
        __init__(*args, **kwargs): initializes a User instance
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Initializes a User instance"""
        super().__init__(*args, **kwargs)
