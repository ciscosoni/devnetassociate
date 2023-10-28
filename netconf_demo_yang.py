from ncclient import manager
from pprint import pprint
import xmltodict
import xml.dom.minidom

router = {"host": "192.168.1.211", "port":"830",
          "username":"soni", "password":"cisco123"}
print(router["host"])
print(router["port"])
print(router["username"])

netconf_filter = """
<filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
   <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
      <interface>
         <name>GigabitEthernet3</name>
      </interface>
   </interfaces>
</filter>
"""

with manager.connect(host=router["host"], port=router["port"], username=router["username"], password = router["password"]) as m:
    for capability in m.server_capabilities:
        print("*" * 50)
        print(capability)
# Get the running config on the filtered out interface
    print ("Connected")
    interface_netconf = m.get_config("running", netconf_filter)
    print("getting running config")
#Below, xml is a property of interface_conf

#XMLDOM for formatting output to xml
xmlDom = xml.dom.minidom.parseString(str(interface_netconf))
print(xmlDom.toprettyxml(indent= " "))
print("*" * 25 + "Break" + "*" * 50)
# XMLTODICT for formatting xml output to a python dictionary
interface_python = xmltodict.parse(interface_netconf.xml)["rpc-reply"]["data"]
# Pprint(interface_python)
name = interface_python
print(name)


