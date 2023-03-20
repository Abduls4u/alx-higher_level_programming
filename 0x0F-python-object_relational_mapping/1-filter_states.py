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
                     passwd=sys.argv[1], db=sys.argv[3])
    cursor = db.cursor()
    query = "SELECT id, name FROM states WHERE name LIKE %s ORDER BY id ASC"
    cursor.execute(query, ('N%',))
    results = cursor.fetchall()
    for row in results:
        print(row)
    cursor.close()
    db.close()
