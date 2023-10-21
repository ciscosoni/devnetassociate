#Parsing XML using Element Tree Library:
import xml.etree.ElementTree as ET

#Get the XML File:
stream = open('/Users/surajsoni/Desktop/DevNet Associate/Codes/sample.xml', 'r')

#parse the data into the Element Tree Object
xml = ET.parse(stream)

#Get the "root" Element object from the ElementTree
root = xml.getroot()

#Iterate through each child of the root Element
for e in root:
    #Print the stringified version of the element
    print(ET.tostring(e))
    print("")

    #print the "ID" attribute of the element object
    print(e.get("Id"))

    