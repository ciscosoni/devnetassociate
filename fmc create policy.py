import json
import sys
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

##### LOGIN #########
url = "https://fmcrestapisandbox.cisco.com"
login_url = '/api/fmc_platform/v1/auth/generatetoken'
headers = {'Content-Type': 'application/json'}
user = 'ciscoson'
pw = 'U_ck7N2S4s0-UaSs'


login_response = requests.post(
    f'{url}{login_url}', auth=(user, pw), verify=False)
# Parse out the headers
resp_headers = login_response.headers
# Grab the token from the response headers
token = resp_headers.get('X-auth-access-token', default=None)
# Set the token in the headers to be used in the next call
headers['X-auth-access-token'] = token

######## CREATE POLICY with Default rule of IPS #########
pol_url = '/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/policy/accesspolicies'

payload = {
    "type": "AccessPolicy",
    "name": "Soni Policy",
    "description": "Soni demo policy",
    "defaultAction": {
        "intrusionPolicy": {
            "name": "Security Over Connectivity",
            "type": "IntrusionPolicy"
        },
        "variableSet": {
            "name": "Default Set",
            "type": "VariableSet"
        },
        "type": "AccessPolicyDefaultAction",
        "logBegin": False,
        "logEnd": True,
        "sendEventsToFMC": True
    }
}

pol_response = requests.post(
    f'{url}{pol_url}', headers=headers, data=json.dumps(payload), verify=False).json()
print(' ******* POLICY CREATED *******')
print(json.dumps(pol_response, indent=2, sort_keys=True))
print(' ******* POLICY CREATED *******')
policyId = pol_response

policy_url = f'/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/policy/accesspolicies/{policyId}'

######## Add Rules to monitor files for Malware #########
rules_url = f'{policy_url}/accessrules'
rules_payload = {
    "sendEventsToFMC": True,
    "action": "ALLOW",
    "enabled": True,
    "type": "AccessRule",
    "name": "Soni DPI Malware Rule",
    "logFiles": True,
    "logBegin": False,
    "logEnd": False,
    "variableSet": {
            "name": "Default Set",
            "type": "VariableSet"
    },
    "sourceNetworks": {
        "objects": [{
            "type": "NetworkGroup",
            "name": "IPv4-Private-All-RFC1918",
        }]
    },
    "filePolicy": {
        "name": "New Malware",
        "type": "FilePolicy"
    }
}

rules_response = requests.post(f'{url}{rules_url}', headers=headers, data=json.dumps(
    rules_payload), verify=False).json()
print(' ******* RULES CREATED *******')
print(json.dumps(rules_response, indent=2, sort_keys=True))
print(' ******* RULES CREATED *******')
### CLEAN UP ####
print('*' * 50 + ' Deleting Policy')

del_response = requests.delete(
    f'{url}{policy_url}', headers=headers,  verify=False).json()
print(json.dumps(del_response, indent=2, sort_keys=True))
