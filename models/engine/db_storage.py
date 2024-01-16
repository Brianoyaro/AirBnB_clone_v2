#!/usr/bin/python3
"""module implementing DataBase storage"""
from os import getenv
from models.base_model import Base
from models.city import City
from models.state import State
from models.place import Place
from models.user import User
from models.amenity import Amenity
from models.review import Review
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from sqlalchemy import create_engine


class DBStorage:
    """class template for the Database"""

    __engine = None
    __session = None

    def __init__(self):
        user = getenv('HBNB_MYSQL_USER')
        passwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        database = getenv('HBNB_MYSQL_DB')
        environment = getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/()'.format(
            user, passwd, host, database), pool_pre_ping=True)
        if environment == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """querries current database"""
        map_ = {'User': User, 'State': State, 'City': City, 'Amenity': Amenity, 'Place': Place, 'Review': Review}
        dictionary = {}
        if cls is not None:
            query = self.__session.query(cls).all()
            for value in query:
                dictionary[value.to_dict()['__class__'] + '.' + value.id] = value
        else:
            for class_ in map_.values():
                query = self.__session.query(class_).all()
                for value in query:
                    dictionary[value.to_dict()['__class__'] + '.' + value.id] = value
        return dictionary

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete from the current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scope_session(Session)

    def close(self):
        """closes db session"""
        self.__session.close()
