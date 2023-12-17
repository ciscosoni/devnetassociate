import requests
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import http.client

conn = http.client.HTTPSConnection("sandboxdnac2.cisco.com")


################ LOGIN ######################
url = "https://sandboxdnac2.cisco.com/dna/system/api/v1/auth/token"


user = 'devnetuser'
pw = 'Cisco123!'

#response = requests.post(url, auth=(user, pw), verify=False).json()
# print(response)
#token = response['Token']

############ GET CLIENT HEALTH STATS ################

# url = "https://sandboxdnac2.cisco.com/dna/intent/api/v1/client-health"

# querystring = {"timestamp": ""}

headers = {
    'content-type': "application/json",
    'authorization': "<Authorization>"
    }

conn.request("POST", "/dna/system/api/v1/auth/token", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
# response = requests.get(url, headers=headers, params=querystring).json()

# #print(json.dumps(response, indent=2, sort_keys=True))

# print(
#     f"Clients: {response['response'][0]['scoreDetail'][0]['clientCount']}")


# scores = response['response'][0]['scoreDetail']

# for score in scores:
#     if score['scoreCategory']['value'] == 'WIRED':
#         print(f"Wired Clients: {score['clientCount']}")
#         score_values = score['scoreList']
#         for score_value in score_values:
#             print(
#                 f"  {score_value['scoreCategory']['value']}: {score_value['clientCount']}")
#     elif score['scoreCategory']['value'] == 'WIRELESS':
#         print(f"Wireless Clients: {score['clientCount']}")
#         score_values = score['scoreList']
#         for score_value in score_values:
#             print(
#                 f"  {score_value['scoreCategory']['value']}: {score_value['clientCount']}")
