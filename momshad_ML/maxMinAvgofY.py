import numpy as np
yList = []
maxVal = -99
minVal = 9999999
total = 0
file = open("O3val")
for i in file:
	if float(i) > maxVal:
		maxVal = float(i)
	if float(i) < minVal:
		minVal = float(i)
	total += float(i) 
	temp = [float(i)]
	yList.append(temp)
print maxVal, minVal, total/len(yList), np.std(np.array(yList))