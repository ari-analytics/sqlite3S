import sqlite3 as lite
import sys
import time

con = lite.connect('sensors.db')

cur = con.cursor()
#	cur.execute("CREATE TABLE Temperatures (Time INT, RNo INT, Temp DOUBLE)")

#cur.execute("INSERT INTO  Temperatures VALUES(int(time.time()),1, 30.0)")
#cur.execute ("INSERT INTO Temperatures ( (?), (?), (?) )", (int(time.time()), 1, 30.0))
cur.executescript("""
	DROP TABLE IF EXISTS TempSensor;
	CREATE TABLE TempSensor (Time INTEGER, RNo INTEGER, Temp REAL);
	INSERT INTO TempSensor VALUES(int(time.time()),1, 30.0);
        """)

con.commit()

