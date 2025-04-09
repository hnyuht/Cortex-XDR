import json
import requests

# Base URL and API credentials
base_url = "https://api-[REMOVE BRACKETS TENANT URL].xdr.us.paloaltonetworks.com/public_api/v1/"
api_key_id = "API ID"
api_key = "API KEY"

def make_request(endpoint, payload=None):
    url = base_url.format(fqdn="your_api_fqdn") + endpoint
    headers = {
        "x-xdr-auth-id": str(api_key_id),
        "Authorization": api_key,
        'Content-Type': "application/json",
        'Accept': "application/json"
    }
    try:
        res = requests.post(url=url, headers=headers, json=payload)
        res.raise_for_status()  # Raise exception for bad response status
        res_json = res.json()
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        res_json = None
    except ValueError as e:
        print(f"Failed to parse response JSON: {e}")
        res_json = None
    return res_json

# Get triage presets
response = make_request("get_triage_presets", payload={"request_data": {}})

# Display the triage presets
if response and 'reply' in response:
    for preset in response['reply']['triage_presets']:
        print(f"UUID: {preset['uuid']}")
        print(f"Name: {preset['name']}")
        print(f"OS: {preset['os']}")
        print(f"Description: {preset['description']}")
        print(f"Created By: {preset['created_by']}")
        print(f"Type: {preset['type']}")
        print("-" * 40)
else:
    print("No response or 'reply' key not found in response.")
