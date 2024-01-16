#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


type_ = getenv("HBNB_TYPE_STORAGE")
class Amenity(BaseModel):
    """amenity class"""
    __tablename__ = "amenities"
    if type_ != 'db':
        name = ""
    else:
        name = Column(String(128), nullable=False)

