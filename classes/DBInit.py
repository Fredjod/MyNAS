#!/usr/local/bin/python3.5
# encoding: utf-8

'''
Created on 30 nov. 2016

@author: home
'''

import sqlite3

try:
    conn = sqlite3.connect("mynas.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
         id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
         name TEXT,
         age INTERGER
    )
    """)
    conn.commit()
finally:
    conn.close

