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
        print("Raw Response Text:", res.text)  # Print raw response for debugging
        res_json = res.json()
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        res_json = None
    except ValueError as e:
        print(f"Failed to parse response JSON: {e}")
        res_json = None
    return res_json

# Test with a basic endpoint, like 'version' or 'status'
response = make_request("version", payload={})

# Print raw response and check if it's valid JSON
if response:
    print("Valid JSON Response:", response)
else:
    print("No valid JSON response or still getting HTML.")
