#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String


type_ = getenv('HBNB_ENV')
class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    if type_ != 'db':
        email = ''
        password = ''
        first_name = ''
        last_name = ''
    else:
        email = Column(String(128), nullabl=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=False)
        last_name = Column(String(128), nullable=False)
        places = relationship("Place", cascade="all, delete, delete-orphan", backref="user")
        reviews = relationship("Review", cascade="all, delete, delete-orphan", backref="user")
