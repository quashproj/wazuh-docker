#!/var/ossec/framework/python/bin/python3
import requests
import sys
import json
import shutil

from requests import packages

# Silence insecure request warning
requests.packages.urllib3.disable_warnings()


# Define the source and destination paths
source_path = sys.argv[1]

# Read the alert file
alert_file = open(sys.argv[1])
alert_json = json.loads(alert_file.read())
alert_file.close()

json_string = json.dumps(alert_json, indent=2)
# file_path = '/tmp/x.json'
# Print the JSON string
# print(json_string)

# Open the file in write mode ('w') and write the string to it
#with open(file_path, 'w') as file:
#    file.write(json_string)
#user = sys.argv[2].split(':')[0]
#api_key = sys.argv[2].split(':')[1]
api_key = sys.argv[2]
hook_url = sys.argv[3]

# Convert the dictionary to a JSON string
alert_level = alert_json['rule']['level']
ruleid = alert_json['rule']['id']
description = alert_json['rule']['description']
agentid = alert_json['agent']['id']
agentname = alert_json['agent']['name']
hash_sha1 = alert_json['data']['virustotal']['source']['sha1']
ip = alert_json['agent']['ip']

# Get OS Type from alert
data = {
    "osType": "linux",
    "hash": hash_sha1,
    "agent_ip": ip
}

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + api_key,
    "X-Argo-E2E": "true"
}

response = requests.post(hook_url, headers=headers, data=dumps(data), verify=False)

print(response.text)
