#converts the raw data into the more accesible val, do this for each file
file = open("WSPD")
lis = []
lis2 = []
for i in file:
	lis = i.split(",")
	lis2.append(lis[3])
file.close()
file2 = open("WSPDval",'w')
for i in lis2:
	file2.write(i + "\n")
file2.close()