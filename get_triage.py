import json
import requests

# NOTES: PLEASE CHECK URL
base_url = "https://api-[REMOVE BRACKETS TENANT URL].xdr.us.paloaltonetworks.com/public_api/v1/"
api_key_id = "API ID"
api_key = "API KEY"

def make_request(endpoint, payload=None):
    url = base_url + endpoint
    headers = {
        "x-xdr-auth-id": str(api_key_id),
        "Authorization": api_key,
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    try:
        res = requests.post(url=url, headers=headers, json=payload)
        res.raise_for_status()
        res_json = res.json()
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        res_json = None
    except ValueError as e:
        print(f"Failed to parse response JSON: {e}")
        res_json = None
    return res_json

# Call the get_triage_presets endpoint
response = make_request("get_triage_presets", {"request_data": {}})
print(json.dumps(response, indent=4))
