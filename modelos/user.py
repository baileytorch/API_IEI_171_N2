from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    username = Column(String(50), nullable=False)
    email = Column(String(255), nullable=False)
    phone = Column(String(25), nullable=True)
    website = Column(String(255), nullable=True)
