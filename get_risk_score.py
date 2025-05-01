import json
import requests

# NOTES: PLEASE CHECK URL
base_url = "https://api-yourfqdn/public_api/v1/"
api_key_id = "SOME_STRING_VALUE"
api_key = "SOME_STRING_VALUE"

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

# Replace with your actual agent_id or collector_uuid
payload_data = {
    "request_data": {
        "agent_ids": ["your-agent-id"],  # Replace with actual agent ID
        "collector_uuid": "your-collector-uuid"  # Optional, replace if needed
    }
}

# Call triage_endpoint instead of get_risk_score
response = make_request("triage_endpoint", payload_data)
print(json.dumps(response, indent=4))
