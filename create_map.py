"""
Nodes are labelled 0-99
x-coordinate, y-coordinate are float values
"""

from random import uniform

obj = open("map.txt",'w+')

for i in range(100):
	xvalue = uniform(0,500) #500 is arbitrary. Any number greater than sqrt(100)=10 would do really
	yvalue = uniform(0,500)
	line = str(i) + " " + str(xvalue) + " " + str(yvalue) + "\n"
	obj.write(line)
