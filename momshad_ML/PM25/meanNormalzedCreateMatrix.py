import numpy as np
import random

def normalizeThisListofList(x):
	yList = []
	maxVal = -99
	minVal = 9999999
	total = 0
	for i in x:
		if i[0] > maxVal:
			maxVal = i[0]
		if i[0] < minVal:
			minVal = i[0]
		total += i[0] 
	theMean = total / len(x)
	for i in x:
		yList.append([(i[0] - theMean)/(maxVal - minVal)] )
	return yList

def normalizeThis(x):
	yList = []
	maxVal = -99
	minVal = 9999999
	total = 0
	for i in x:
		if i > maxVal:
			maxVal = i
		if i < minVal:
			minVal = i
		total += i 
	theMean = total / len(x)
	for i in x:
		yList.append((i - theMean)/(maxVal - minVal) )
	return yList





file = open("TMPval")
TMP = []
for i in file:
	TMP.append(float(i))
TMP = normalizeThis(TMP)

file = open("WDIRval")
WDIR = []
for i in file:
	WDIR.append(float(i))
WDIR = normalizeThis(WDIR)

file = open("WSPDval")
WSPD = []
for i in file:
	WSPD.append(float(i))
WSPD = normalizeThis(WSPD)

matrixList = []
for i in range( len(TMP) ):
	temp = []
	temp.append(1)
	temp.append(TMP[i])
	temp.append(WDIR[i])
	temp.append(WSPD[i])
	matrixList.append(temp)
featureMatrix = np.matrix(matrixList)
yMatrixList = []
file = open("PM25val")
for i in file:
	temp = [float(i)]
	yMatrixList.append(temp)
yMatrixList = normalizeThisListofList(yMatrixList)							# thetaMatrix = 5*1
yMatrix = np.matrix(yMatrixList)        #yMatrix is x*1 and featureMatrix x*5


#start MultiVariate Polynomial regression
thetaMatrix = np.matrix([  [random.uniform(0.0, 1000.0)], [random.uniform(0.0, 1000.0)], [random.uniform(0.0, 1000.0)], [random.uniform(0.0, 1000.0)] ])
def costFunction(x):
	totalErr = 0
	for i in range( len(yMatrix) ):
		hx = featureMatrix[i,] * x 
		totalErr += (hx - yMatrix[i, 0]) ** 2
	return totalErr / (2 * len(yMatrix))
x = np.linalg.inv(featureMatrix.transpose() * featureMatrix) * featureMatrix.transpose() * yMatrix
print  "cost func s " + str(costFunction(x))
print x
print featureMatrix[1, ] * x


	






