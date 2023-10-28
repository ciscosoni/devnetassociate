from ncclient import manager
import pprint
import xmltodict
import xml.dom.minidom

router = {
   'ip': '192.168.1.211',
   'port': '830',
   'username': 'soni',
   'password': 'cisco123'
}

m = manager.connect(host=router['ip'], port=router['port'], username=router['username'],
                    password=router['password'], device_params={'name':'iosxe'}, hostkey_verify=False)

netconf_filter = """
<filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
   <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
      <interface>
         <name>GigabitEthernet1</name>
      </interface>
   </interfaces>
</filter>
"""

running_config = m.get(netconf_filter)

running_config_xml = xmltodict.parse(running_config.xml)["rpc-reply"]["data"]
print(xml.dom.minidom.parseString(str(running_config)).toprettyxml())