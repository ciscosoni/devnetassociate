import requests
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
####### LOGIN ###########
url = "https://192.168.1.241:443/api/aaaLogin.json"

payload = {
    "aaaUser": {
        "attributes": {
            "name": "admin",
            "pwd": "admin@123"
        }
    }
}
headers = {
    'Content-Type': "application/json"
}

response = requests.post(url, data=json.dumps(
    payload), headers=headers, verify=False).json()

# print(json.dumps(response, indent=2, sort_keys=True))

# PARSE TOKEN AND SET COOKIE
token = response['imdata'][0]['aaaLogin']['attributes']['token']
cookie = {}
cookie['APIC-cookie'] = token


######### GET APN ##############
# GET APPLICATION PROFILE
url = "https://192.168.1.241:443/api/node/mo/uni/tn-Python-Tenant.json"

headers = {
    'cache-control': "no-cache"
}

get_response = requests.get(
    url, headers=headers, cookies=cookie, verify=False).json()

print(json.dumps(get_response, indent=2, sort_keys=True))


########## UPDATE APN DESCRIPTION #############
# SET DESCRIPTION
post_payload = {
    "fvAp": {
        "attributes": {
            "descr": "This Description is configured via Python",
            "dn": "uni/tn-Test-Tenant1/ap-Test-AP1"
        }
    }
}

post_response = requests.post(
    url, headers=headers, cookies=cookie, verify=False, data=json.dumps(post_payload)).json()

get_response = requests.get(
    url, headers=headers, cookies=cookie, verify=False).json()

print(json.dumps(get_response, indent=2, sort_keys=True))
