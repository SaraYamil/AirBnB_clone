#!/usr/bin/python3

""" define the BaseModel class module"""

import models

from uuid import uuid4
from datetime import datetime

DATE_ISO8601_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """
    Represents the BaseModel class

    Attributes:
        id (str): A unique identifier generated for the instance of BaseModel.
        created_at (datetime): A datetime object representing the creation time of the BaseModel instance.
        updated_at (datetime): A datetime object representing the time of the last update to the BaseModel instance.

    Methods:
        __init__(*args, **kwargs): initializes a new instance of basemodel
        __str__(): returns a string representation of the BaseModel instance
        save(): updates attribute with the current datetime
        to_dict(): returns a dictionary containing all keys and their values
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes a new BaseModel instance

        Args:
            *args: unused
            **kwargs: kwargs (dict): Key/value pairs of attributes.

        Returns:
            None
        """
        if kwargs:
            for key in kwargs:
                if key != "__class__":
                    setattr(self, key, kwargs[key])
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(
                        kwargs[key], DATE_ISO8601_FORMAT))
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

            # Add a call to the new(self) method on storage
            models.storage.new(self)

    def __str__(self):
        """
        Return the print/str representation of the BaseModel instance
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """
        Updates the updated_at attribute with the current datetime

        Returns:
            None
        """
        self.updated_at = datetime.now()
        models.storage.save()  # Call the save() method of the storage instance

    def to_dict(self):
        """
        Returns the  dictionary of  keys/values of the BaseModel
        instance

        """
        obj_dict = self.__dict__.copy()

        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()

        return obj_dict
