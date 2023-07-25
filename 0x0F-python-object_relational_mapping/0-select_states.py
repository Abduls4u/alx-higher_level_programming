#!/usr/bin/python3
''' Script that lists all states from the database hbtn_0e_0_usa
Usage:
    ./0-select_states.py
Author:
    Abdulsalam Abdulsomad .A. - July 25th, 2023.
'''
import MySQLdb
import sys


def list_states():
    '''lists all the states in the db'''

    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states")
    states = cursor.fetchall()
    for state in states:
        print(state)


list_states()
