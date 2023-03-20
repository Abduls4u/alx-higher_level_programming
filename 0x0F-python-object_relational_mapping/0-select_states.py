#!/usr/bin/python3
''' A module that contains  script that lists all states from the
database hbtn_0e_0_usa.
Usage:
    ./0-select_states.py
Author:
    Abdulsalam Abdulsomad .A. - March 20th, 2023.
'''
import MySQLdb as sql
import sys


if __name__ == "__main__":
    db = sql.connect(user=sys.argv[1],
                     passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT id, name FROM states ORDER BY id ASC")
    results = cursor.fetchall()
    for row in results:
        print(row)
    cursor.close()
    db.close()
