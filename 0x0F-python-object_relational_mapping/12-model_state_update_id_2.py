#!/usr/bin/python3
''' A module that contains  script that upsates State object where id==2.
Usage:
    ./12-model_state_update_id_2.py
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
    state_to_update = session.query(State).filter(State.id == 2).first()
    state_to_update.name = 'New Mexico'
    session.commit()
