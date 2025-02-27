#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"

    if getenv("HBNB_TYPE_STORAGE") != 'db':
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            from models import storage
            ans = []
            for value in storage.all(Review).values():
                if value.place_id == self.id:
                    ans.append(value)
            return ans

        @property
        def amenities(self):
            from models import storage
            ans = []
            for value in storage.all(Amenity).values():
                if value.id == self.amenity_ids:
                    ans.append(value)
            return ans

        @amenities.setter
        def amenities(self, obj):
            from models.amenity import Amenity
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)
    else:
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship("Review", cascade="all, delete, delete-orphan", backref="place")

        place_amenity = Table(
                "place_amenity",
                Base.metadata,
                Column("place_id", String(60), ForeignKey("places.id"), primary_key=True, nullable=False),
                Column("amenity_id", String(60), ForeignKey("amenities.id"), primary_key=True, nullable=False))
        amenities = relationship("Amenity", secondary=place_amenity, viewonly=False, backref="places")
