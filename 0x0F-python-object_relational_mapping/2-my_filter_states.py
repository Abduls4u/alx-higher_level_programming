#!/usr/bin/python3
''' Script that lists all states from the database hbtn_0e_0_usa
that matches the 4th command line arguments
Usage:
    ./2-my_filter_states.py
Author:
    Abdulsalam Abdulsomad .A. - July 25th, 2023.
'''
import MySQLdb
import sys


def list_states_name():
    '''lists all the states in the db that matches sys.argv[4] '''

    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE '{}'"
                   .format(sys.argv[4]))
    states = cursor.fetchall()
    for state in states:
        print(state)


if __name__ == '__main__':
    list_states_name()
