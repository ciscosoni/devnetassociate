import requests
import json
import pprint

url = "https://dashboard.meraki.com/api/v0/organizations"

payload = {}
headers = {
  'X-Cisco-Meraki-API-Key': 'eb26907c5075422df66da7310131072b4ac6474d'
}

response = requests.get( url, headers=headers, data=payload).json()

print(response)

