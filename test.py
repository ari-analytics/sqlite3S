#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys
import time

try:
    con = lite.connect('rasp.db')

    cur = con.cursor()  
    time1 = int(time.time())
    print time1
    print time.time()
    cur.executescript("""
        DROP TABLE IF EXISTS TempSensor;
        CREATE TABLE TempSensor(hist INT, room INT, Temp REAL);
        INSERT INTO TempSensor VALUES(1,1,30.0);
        INSERT INTO TempSensor VALUES(1,1,29.4);
        INSERT INTO TempSensor VALUES(1,1,30.3);
        INSERT INTO TempSensor VALUES(1,1,30.4);
        INSERT INTO TempSensor VALUES(1,1,35.5);
        INSERT INTO TempSensor VALUES(1,1,32.4);
        INSERT INTO TempSensor VALUES(1,1,32.4);
        INSERT INTO TempSensor VALUES(1,1,32.5);
        """)

    con.commit()
    
except lite.Error, e:
    
    if con:
        con.rollback()
        
    print "Error %s:" % e.args[0]
    sys.exit(1)
    
finally:
    
    if con:
        con.close() 

