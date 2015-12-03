import urllib2
import urllib
import lxml.html as Scraper
import os.path

pageSourceList1 = [
"CO",
"COm",
"NO2",
"NO2m",
"NO",
"NOm",
"NOX", "NOXm",
"O3",
"O3m", "PM10",
"DUST",
"PM25",
"FINE",
"SO2",
"SO2m",
"BENZ",
"BENZm"]
pageSourceList2 = [
"RAIN",
"RHUM",
"TMP",
"WDIR",
"WSPD" ]

baseUrl = "http://www.londonair.org.uk/london/asp/dataspecies.asp?species="

def printVals(x):
	hashMap = {}
	for i in x:
		response = urllib2.urlopen(baseUrl + i)
		page_source = response.read()
		doc = Scraper.fromstring(page_source)
		elements = doc.xpath('//*[@id="site1"]/option')
		codes = map(lambda x: x.get('value'), elements)
		hashMap[i] = codes
	hashMap2 = {}
	for feature in hashMap.keys():
		for area in hashMap[feature]:
			if area in hashMap2.keys():
				hashMap2[area] += 1
			else:
				hashMap2[area] = 1
	tmp = []
	for area in hashMap2.keys():
		if hashMap2[area] == 6:
			tmp.append(area)
	print "START"
	print [x[0]] + tmp
	print "END"

for i in pageSourceList1:
	printVals([i] + pageSourceList2)




#to do store parse each page_source and extract the <select name = "site1"
