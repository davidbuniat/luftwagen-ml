import urllib2
import urllib
import lxml.html as Scraper
import os.path

pageSourceList = [
"CO",
"COm",
"NO2",
"NO2m",
"NO",
"NOm",
"NOX",
"NOXm",
"O3",
"O3m",
"PM10",
"DUST",
"PM25",
"FINE",
"SO2",
"SO2m",
"BENZ",
"BENZm",
"BP",
"RAIN",
"RHUM",
"SOLR",
"TMP",
"WDIR",
"WSPD"]
hashMap = {}
baseUrl = "http://www.londonair.org.uk/london/asp/dataspecies.asp?species="
for i in pageSourceList:
	response = urllib2.urlopen(baseUrl + i)
	page_source = response.read()

	doc = Scraper.fromstring(page_source)
	elements = doc.xpath('//*[@id="site1"]')
	codes = map(lambda x: x.get('value'), elements)
	hashMap[pageSourceList] = codes

print hashMap

#to do store parse each page_source and extract the <select name = "site1"
