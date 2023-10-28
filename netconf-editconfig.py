from ncclient import manager

router = {"host": "192.168.1.211", "port": "830",
          "username": "soni", "password": "cisco"}

config_template = open(
    "E:/dev/CodeSamples/Python/Networking/IOS-XE/ios_config.xml").read()

netconf_config = config_template.format(
    interface_name="GigabitEthernet2", interface_desc="daniyal")

with manager.connect(host=router["host"], port=router["port"], username=router["username"], password=router["password"], hostkey_verify=False) as m:
    device_reply = m.edit_config(netconf_config, target="running")
    print(device_reply)
