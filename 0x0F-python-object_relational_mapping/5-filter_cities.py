#!/usr/bin/python3
''' A module that contains  script that lists all cities in a
state from the database.
Usage:
    ./5-filter_cities.py
Author:
    Abdulsalam Abdulsomad .A. - March 20th, 2023.
'''
import MySQLdb as sql
import sys


if __name__ == "__main__":
    db = sql.connect(host="localhost", port=3306, user=sys.argv[1],
                     passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    query = "SELECT * FROM cities INNER JOIN states ON \
             state_id = states.id WHERE states.name LIKE %s \
             ORDER BY cities.id ASC"
    cursor.execute(query, (sys.argv[4],))
    results = cursor.fetchall()
    print(", ".join([c[2] for c in results if c[4] == sys.argv[4]]))
    cursor.close()
    db.close()
