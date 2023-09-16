#!/usr/bin/python3
"""BaseModel class"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Representation of BaseModel"""

    def __init__(self, *args, **kwargs):
        """Init a new BaseModel

        Args:
            *args (any): won’t be used
            **kwargs (dict): Key/value of attributes
        """
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        tformat = "%Y-%m-%dT%H:%M:%S.%f"
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tformat)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def __str__(self):
        """Print representation of the BaseModel"""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)

    def save(self):
        """updates the attribute updated_at with the current datetime """
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values
        of __dict__ of the BaseModel instance
        """
        obj_dict = self.__dict__.copy()
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        obj_dict["__class__"] = self.__class__.__name__
        return obj_dict
