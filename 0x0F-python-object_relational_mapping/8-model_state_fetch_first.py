#!/usr/bin/python3
''' A module that contains  script that lists the first State objects.
Usage:
    ./8-model_state_fetch_first.py
Author:
    Abdulsalam Abdulsomad .A. - March 25th, 2023.
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
    states = session.query(State.id, State.name).order_by(State.id).first()
    if states is not None:
        print(f'{states.id}: {states.name}')
    else:
        print('Nothing')
