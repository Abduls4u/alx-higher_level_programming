#!/usr/bin/python3
''' A module that contains  script that lists all states with
letter N from the database hbtn_0e_0_usa.
Usage:
    ./1-filter_states.py
Author:
    Abdulsalam Abdulsomad .A. - March 20th, 2023.
'''
import MySQLdb as sql
import sys


if __name__ == "__main__":
    db = sql.connect(host="localhost", port=3306, user=sys.argv[1],
                     passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    query = "SELECT id, name FROM states WHERE name=%s ORDER BY id ASC"
    cursor.execute(query, (sys.argv[4],))
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db.close()
