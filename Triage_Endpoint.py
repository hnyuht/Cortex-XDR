import json
import requests

# === CONFIGURE YOUR DETAILS HERE ===
base_url = "https://api-yourfqdn/public_api/v1/"  # Replace 'yourfqdn' with actual tenant
api_key_id = "YOUR_API_ID"                        # Replace with your actual API ID
api_key = "YOUR_API_KEY"                          # Replace with your actual API key

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
        try:
            return res.json()
        except ValueError:
            print("⚠️ Response not in JSON format. Raw response below:")
            print(res.text)
            return None
    except requests.exceptions.RequestException as e:
        print(f"❌ Request failed: {e}")
        return None

# === TRIAGE ENDPOINT REQUEST ===
triage_payload = {
    "request_data": {
        "agent_ids": ["REPLACE_WITH_AGENT_ID"],         # Example: ["abc123"]
        "collector_uuid": "REPLACE_WITH_COLLECTOR_UUID" # Example: "uuid-xyz"
    }
}

response = make_request("triage_endpoint", triage_payload)

# === HANDLE RESPONSE ===
if response:
    print("✅ Triage Data Received:")
    print(json.dumps(response, indent=2))
else:
    print("❌ No valid response received.")
