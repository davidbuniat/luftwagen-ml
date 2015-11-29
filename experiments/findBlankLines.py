files = [ "WSPDval", "WDIRval", "TMPval", "RAINval","PM25val"] #
count = 0
blankLines = []
for i in files:
	file = open(i)
	for line in file:
		if line == "\n":
			print "here"
			if count+1 not in blankLines:
				blankLines.append(i + " " + str(count+1))
		count += 1
	count = 0
print blankLines
