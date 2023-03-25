#!/usr/bin/python3
''' A module that contains  script that creates a Table object(Cit
y) in the database.
Usage:
    ./model_states.py
Author:
    Abdulsalam Abdulsomad .A. - March 20th, 2023.
'''
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State


class City(Base):
    '''A class that creates a table(city) and inherits from Base'''
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id))
