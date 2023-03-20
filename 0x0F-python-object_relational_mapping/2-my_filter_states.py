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


db = sql.connect(host="localhost", port=3306, user="root",
                 passwd="root", db="hbtn_0e_0_usa")
cursor = db.cursor()
query = "SELECT id, name FROM states WHERE name=%s ORDER BY id ASC"
cursor.execute(query, (sys.argv[4],))
results = cursor.fetchone()
print(results)
cursor.close()
db.close()
