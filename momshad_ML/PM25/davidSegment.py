import numpy as np
segmentvar = 150


file = open("TMPval")
TMP = []
for i in file:
	TMP.append(float(i))

file = open("WDIRval")
WDIR = []
for i in file:
	WDIR.append(float(i))

file = open("WSPDval")
WSPD = []
for i in file:
	WSPD.append(float(i))

yList = []
file = open("PM25val")
for i in file:
	temp = [float(i)]
	yList.append(temp)

matrixListTrain = []
matrixListTest = []
yListTrain = []
yListTest = []
for i in range(segmentvar):
	yListTrain.append(yList[i])
	temp = []
	temp.append(TMP[i])
	temp.append(WDIR[i])
	temp.append(WSPD[i])
	matrixListTrain.append(temp)
for i in range(segmentvar, len(RAIN), 1):
	yListTest.append(yList[i])
	temp = []
	temp.append(TMP[i])
	temp.append(WDIR[i])
	temp.append(WSPD[i])
	matrixListTest.append(temp)


print matrixListTrain
print yListTrain
print matrixListTest
print yListTest
npmatrixListTrain = np.array(matrixListTrain)
npyListTrain = np.array(yListTrain)
npmatrixListTest = np.array(matrixListTest)
npyListTest = np.array(yListTest)
