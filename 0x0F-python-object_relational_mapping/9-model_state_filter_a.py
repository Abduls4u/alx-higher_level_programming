#!/usr/bin/python3
''' A module that contains  script that lists all State objects
with letter (a).
Usage:
    ./9-model_state_filter_a.py
Author:
    Abdulsalam Abdulsomad .A. - March 24th, 2023.
'''
import sys
from sqlalchemy.orm import Session
from model_state import Base, State
from sqlalchemy import (create_engine)


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(bind=engine)
    states = session.query(State).filter(State.name.like('%a%'))\
                                 .order_by(State.id)
    for state in states:
        print(f'{state.id}: {state.name}')
