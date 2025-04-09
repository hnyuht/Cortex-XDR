import json
import requests

# Set your actual tenant FQDN and API credentials here
base_url = "https://api-yourfqdn/public_api/v1/"
api_key_id = "YOUR_API_ID"
api_key = "YOUR_API_KEY"

def make_request(endpoint, payload=None):
    url = base_url + endpoint
    headers = {
        "x-xdr-auth-id": str(api_key_id),
        "Authorization": api_key,
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    try:
        res = requests.post(url, headers=headers, json=payload)
        res.raise_for_status()
        return res.json()
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
    except ValueError as e:
        print(f"Failed to parse response JSON: {e}")
    return None

# Payload for triage_endpoint
triage_payload = {
    "request_data": {
        "agent_ids": ["agent_id_123"],
        "collector_uuid": "collector_uuid_abc"
    }
}

# Call triage_endpoint
response = make_request("triage_endpoint", triage_payload)

# Display response
if response:
    print(json.dumps(response, indent=2))
else:
    print("No data received.")
