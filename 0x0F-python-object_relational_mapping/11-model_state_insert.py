#!/usr/bin/python3
''' A module that contains  script that adds a new state to the State object
Usage:
    ./11-model_state_insert.py
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
    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()
    print(new_state.id)
