import serial
import numpy as np
from matplotlib import pyplot as plt
ser = serial.Serial('COM3', 9600)
 
plt.ion() # set plot to animated
f = open("heart.txt", "w")
ydata = [0] * 1000
ax1=plt.axes()  
counter=0
# make plot
line, = plt.plot(ydata)
plt.ylim([0,3500])
maxd = 2500.0
lastd = 0
# start data collection
data = [0,0]
timer= 20.0
while True:
	lastdata = data
	data = ser.readline() # read data from serial 
	#print('Receiving...'+data)
	data = data.rstrip();
	f.write(data+"\n")
	
	data = data.split(",")
	ydata.append(data[0])
	if lastd==0:
		lastd = float(data[1])-1
	maxd = maxd*0.5 + 0.5*float(max(ydata))
	#print timer
	#print lastdata[0], data[0],lastdata[1],data[1],maxd,lastd
	if ((float(lastdata[0])/0.9>float(maxd)) & (float(data[0])<float(lastdata[0])) & (float(lastd)+timer/2<float(data[1]))):
		timer = timer*0.5 + 0.5*(float(data[1])-float(lastd))
		lastd=data[1]
		print "heart rate:"+str(int(60000/timer))
	del ydata[0]
	line.set_xdata(np.arange(len(ydata)))
	line.set_ydata(ydata)  # update the data
	counter+=1
	if counter>50:
		counter=0
		plt.draw() # update the plot
		plt.pause(10e-10)
f.close()