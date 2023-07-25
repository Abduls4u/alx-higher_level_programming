#!/usr/bin/python3
''' Script that lists all states from the database hbtn_0e_0_usa
that starts with N
Usage:
    ./1-filter_states.py
Author:
    Abdulsalam Abdulsomad .A. - July 25th, 2023.
'''
import MySQLdb
import sys


def list_states_N():
    '''lists all the states in the db that starts with N '''

    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE %s"
    place_holder_value = "N%"
    cursor.execute(query, (place_holder_value, ))
    states = cursor.fetchall()
    for state in states:
        print(state)


if __name__ == '__main__':
    list_states_N()
