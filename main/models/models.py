from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from models.database import Base

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=True, unique=True)
    posts = relationship("Post", backref='user')

    def repr(self):
        return self.name

class Post(Base):
    __tablename__ = 'word'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    title = Column(String(30), nullable=False)
    img = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now())