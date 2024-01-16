#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, String
from os import getenv


type_ = getenv("HBNB_ENV")
class Review(BaseModel, Base):
    """ Review classto store review information """
    __tablename__ = "reviews"
    if type_ != 'db':
        place_id = ""
        user_id = ""
        text = ""
    else:
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey("places,id"), nullable=False)
        user_id = Column(Striing(60), ForeignKey("users.id"), nullable=False)
