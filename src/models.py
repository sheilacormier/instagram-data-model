import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table user
    id = Column(Integer, primary_key=True)
    username = Column(String(100), unique=True, nullable=False)
    password = Column(String(20), nullable=False)
    firstname = Column(String(50))
    lastname = Column(String(50))
    email = Column(String(100), nullable=False, unique=True)
    posts = relationship("Post", backref="user")
    comments = relationship("Comment", backref="user")

class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the post   
    id = Column(Integer, primary_key=True)
    # relationship for 
    user_id = Column(String(50), ForeignKey('user.id'))
    comment_text = relationship("Comment", backref="post")

class Comment(Base):
    __tablename__ = 'comment'
    # Here we define columns for the comment   
    id = Column(Integer, primary_key=True)
    # relationship for 
    user_id = Column(String(50), ForeignKey('user.id'))
    post_id = Column(String(50), ForeignKey('user.id'))
    comment_text = Column(String(500))

class Media(Base):
    __tablename__ = 'media'
    # Here we define columns for the media   
    id = Column(Integer, primary_key=True)
    # relationship for 
    Type = Column(String(50))
    url = Column(String)
    post_id = Column(Integer, ForeignKey('user.id'))


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')