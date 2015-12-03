import xml.etree.ElementTree as xml
tree = xml.parse('sites.xml')
file2 = open("siteFile",'w')
for i in tree.getroot():
	file2.write(str(i.attrib["value"]) + " -> " + i.text + "\n")
