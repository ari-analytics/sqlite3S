import matplotlib.pyplot as plt
import urllib
import time
#from drawnow import *
import sqlite3 as lite
import sys
link = "http://192.168.0.104:8080"
f = urllib.urlopen(link)
x_axis = int(time.time())
# connect to db
con = lite.connect('rasp.db')
cur = con.cursor()
cur.executescript ("""
	DROP TABLE IF EXISTS TempSensor;
        CREATE TABLE TempSensor(hist INT, room INT, Temp REAL);
        """)


room = 1
#def save_temp(room,temp):
#	x_axis = int(time.time())
#        cur.execute("INSERT INTO TempSensor VALUES(1,1,30)")
#        con.commit()

while True:
	try:
		f = urllib.urlopen(link)
		temperature = f.read()
		time.sleep(1)
		print temperature
		x_axis = int(time.time())
                temp = (x_axis, room, temperature)
	        print "tempsets=  ",temp
		cur.execute("INSERT INTO TempSensor VALUES(?,?,?)",temp)
		con.commit()
	except KeyboardInterrupt:
		break
#	finally:
#		if con:
#			con.close()

#tempC = []
#def makeFig():
#	plt.ylim(20,80)
#	plt.title('Temperature Streaming')
#	plt.grid(True)
#	plt.plot(tempC, 'ro-',label='Degree C')
#	plt.legend(loc='upper left')
#cnt = 0
#while True:
#	f = urllib.urlopen(link)
#	temperature = f.read()
#	tempC.append(temperature)
#	drawnow(makeFig)
#	plt.pause(.0001)
#	cnt = cnt+1
#	if (cnt>50):
#		tempC.pop(0)
#	print "temperature= " , temperature
 


