import numpy as np
segmentvar = 160

file = open("RAINval")
RAIN = []
for i in file:
	RAIN.append(float(i))

file = open("RHUMval")
RHUM = []
for i in file:
	RHUM.append(float(i))


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
file = open("O3val")
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
	for i in range(len(RAIN)):
		#arr[i] = (arr[i] - mean_n)/(max_n-min_n)
		arr[i] = arr[i]/max_n
	return arr


RAIN = normalize(RAIN)
RHUM = normalize(RHUM)
TMP = normalize(TMP)
WDIR = normalize(WDIR)
WSPD = normalize(WSPD)
yList = normalize(yList)

for i in range(segmentvar):
	yListTrain.append(yList[i])
	temp = []
	temp.append(RAIN[i])
	temp.append(RHUM[i])
	temp.append(TMP[i])
	temp.append(WDIR[i])
	temp.append(WSPD[i])
	matrixListTrain.append(temp)

for i in range(segmentvar, len(RAIN), 1):
	yListTest.append(yList[i])
	temp = []
	temp.append(RAIN[i])
	temp.append(RHUM[i])
	temp.append(TMP[i])
	temp.append(WDIR[i])
	temp.append(WSPD[i])
	matrixListTest.append(temp)


#print matrixListTrain
#print yListTrain
#print matrixListTest
#print yListTest
npmatrixListTrain = np.array(matrixListTrain)
npyListTrain = np.array(yListTrain)
npmatrixListTest = np.array(matrixListTest)
npyListTest = np.array(yListTest)
