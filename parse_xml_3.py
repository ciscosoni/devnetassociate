# Parse data using "xmltodict"
import xmltodict

#Get the XML file data
stream = open('/Users/surajsoni/Desktop/DevNet Associate/Codes/sample.xml', 'r')

#parse the XML file into an OrderedDict
xml = xmltodict.parse(stream.read())

for e in xml:
    print(e)


