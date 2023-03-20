#!/usr/bin/python3
''' A module that contains  script that lists all states with name
 matching sys.argv[4] from the database hbtn_0e_0_usa.
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
    cursor.execute("SELECT id, name FROM states WHERE\
                   name='{}' ORDER BY id ASC".format(sys.argv[4]))
    results = cursor.fetchall()
    for row in results:
        if row[1] == sys.argv[4]:
            print(row)
    cursor.close()
    db.close()
