import requests
import json


url = "https://dashboard.meraki.com/api/v0/organizations/549236/networks"

payload = {}
headers = {
  'X-Cisco-Meraki-API-Key': 'eb26907c5075422df66da7310131072b4ac6474d'
}

response = requests.request("GET", url, headers=headers, data=payload).json()

print(json.dumps (response, indent=2, sort_keys=True))
