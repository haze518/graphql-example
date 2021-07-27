from sqlalchemy import (
    Column,
    Integer,
    String,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey

Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)


class Films(Base):
    __tablename__ = 'films'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)


class Likes(Base):
    __tablename__ = 'likes'

    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), primary_key=True)
    film_id = Column(Integer, ForeignKey('films.id', ondelete='CASCADE'), primary_key=True)
    user = relationship('Users', foreign_keys=[user_id])
    films = relationship('Films', foreign_keys=[film_id])
