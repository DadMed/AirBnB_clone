#!/usr/bin/python3
"""
Module for the Amenity class.
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    This class represents an amenity.


    Attributes:
        name (str): A string indicating the name of the amenity.
    """

    name = ""