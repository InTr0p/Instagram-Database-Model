import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()


class user(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)


class followers(Base):
    __tablename__ = 'followers'
    id = Column(Integer, primary_key=True)
    user_to_id = Column(Integer, ForeignKey('user.id'))
    userto_id = Column(Integer, ForeignKey('user.id'))


class media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    media_type = Column(String(250), nullable=False)
    url = Column(String(250))
    post_id = Column(Integer, ForeignKey('post.id'))


class post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    location_in_coordinates = Column(String(250))
    user_id = Column(Integer, ForeignKey('user.id'))


class comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250))
    author_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    def to_dict(self):
        return {}


# Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
