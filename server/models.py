from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Episode(Base):
    __tablename__ = 'episodes'
    
    id = Column(Integer, primary_key=True)
    date = Column(String)
    number = Column(Integer)
    
    appearances = relationship("Appearance", back_populates="episode", cascade="all, delete-orphan")
    guests = relationship("Guest", secondary="appearances", back_populates="episodes")


class Guest(Base):
    __tablename__ = 'guests'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    occupation = Column(String)
    
    appearances = relationship("Appearance", back_populates="guest", cascade="all, delete-orphan")
    episodes = relationship("Episode", secondary="appearances", back_populates="guests")


class Appearance(Base):
    __tablename__ = 'appearances'
    
    id = Column(Integer, primary_key=True)
    rating = Column(Integer)
    episode_id = Column(Integer, ForeignKey('episodes.id'))
    guest_id = Column(Integer, ForeignKey('guests.id'))
    
    episode = relationship("Episode", back_populates="appearances")
    guest = relationship("Guest", back_populates="appearances")
