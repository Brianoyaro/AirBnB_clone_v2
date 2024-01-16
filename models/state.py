#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    if getenv("HBNB_TYPE_STORAGE") != 'db':
        name = ""

        @property
        def cities(self):
            """returns list of City instances with state_id\
                    equals current State.id"""
            from models import storage
            cities_ = storage.all(City)
            ans = []
            for val in cities_.values():
                if val.state_id == self.id:
                    ans.append(val)
            return ans
    else:
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="all, delete, delete-orphan", backref="states")
