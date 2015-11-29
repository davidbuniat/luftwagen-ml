import numpy as np
segmentvar = 1500


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


def normalize(arr):
	max_n = np.amax(arr)
	min_n = np.amin(arr)
	mean_n = np.mean(arr)
	print(max_n)
	for i in range(len(TMP)):
		#arr[i] = (arr[i] - mean_n)/(max_n-min_n)
		arr[i] = arr[i]/max_n
	return arr


TMP = normalize(TMP)
WDIR = normalize(WDIR)
WSPD = normalize(WSPD)
yList = normalize(yList)

for i in range(segmentvar):
	yListTrain.append(yList[i])
	temp = []
	temp.append(TMP[i])
	temp.append(WDIR[i])
	temp.append(WSPD[i])
	matrixListTrain.append(temp)
for i in range(segmentvar, len(TMP), 1):
	yListTest.append(yList[i])
	temp = []
	temp.append(TMP[i])
	temp.append(WDIR[i])
	temp.append(WSPD[i])
	matrixListTest.append(temp)



npmatrixListTrain = np.array(matrixListTrain)
npyListTrain = np.array(yListTrain)
npmatrixListTest = np.array(matrixListTest)
npyListTest = np.array(yListTest)
