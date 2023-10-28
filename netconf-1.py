from ncclient import manager


router = {"host": "192.168.1.211", "port": "830",
          "username": "soni", "password": "cisco123"}

with manager.connect(host=router["host"], port=router["port"], username=router["username"], password=router["password"], hostkey_verify=False) as m:
   print('Connected')
