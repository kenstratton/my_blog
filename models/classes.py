from sqlalchemy import *
from sqlalchemy.orm import relationship
from datetime import datetime
from models.database import Base

# User class holds info of an actual user and relationships with multiple posts.
class User(Base):
    __tablename__ = "user"

    # Attributes
    id = Column(Integer, primary_key=True)
    name = Column(String(30), unique=True)
    hashed_password = Column(String(128))
    posts = relationship("Post", backref='user')

    def __init__(self, name=None, hashed_password=None):
        self.name = name
        self.hashed_password = hashed_password

    def repr(self):
        return self.name

# Post class is crafted off by and belongs to an actual user.
class Post(Base):
    __tablename__ = 'word'

    # Attributes
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    title = Column(String(50))
    detail = Column(String(1000))
    created_at = Column(DateTime, default=datetime.now())

    def __init__(self, user_id=None, title=None, detail=None):
        self.user_id = user_id
        self.title = title
        self.detail = detail