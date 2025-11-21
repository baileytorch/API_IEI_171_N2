from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    body = Column(String(255), nullable=False)
    userId = Column(Integer, ForeignKey('users.id'), nullable=False)
