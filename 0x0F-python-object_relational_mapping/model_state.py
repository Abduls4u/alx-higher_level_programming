#!/usr/bin/python3
''' A module that contains  script that lists all cities in a
state from the database.
Usage:
    ./model_states.py
Author:
    Abdulsalam Abdulsomad .A. - March 20th, 2023.
'''
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    '''A class that creates a table(states) and inheruts from Base'''
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
