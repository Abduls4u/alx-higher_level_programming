#!/usr/bin/python3
''' A module that contains  script that lists all city objects.
Usage:
    ./14-model_city_fetch_by_state.py
Author:
    Abdulsalam Abdulsomad .A. - March 24th, 2023.
'''
import sys
from sqlalchemy.orm import Session
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(bind=engine)
    cities = session.query(City, State).join(State).order_by(City.id).all()
    for city, state in cities:
        print('{}: ({}) {}'.format(state.name, (city.id), city.name))
