import json
import requests

# === CONFIGURATION ===
base_url = "https://api-yourtenant.xdr.us.paloaltonetworks.com/public_api/v1/"  # Replace with actual tenant URL
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
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()  # Will raise HTTPError for bad responses (4xx or 5xx)
        try:
            return response.json()
        except ValueError:
            return {"error": "Response not in JSON format", "raw": response.text}
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

def handle_triage(agent_ids, collector_uuid):
    payload = {
        "request_data": {
            "agent_ids": agent_ids,
            "collector_uuid": collector_uuid
        }
    }

    result = make_request("triage_endpoint", payload)
    if result and "error" in result:
        return result  # Return error details if present
    if not result or "reply" not in result:
        return {"error": "No 'reply' in response", "raw": result}

    reply = result["reply"]
    return {
        "action_id": reply.get("group_action_id"),
        "success": reply.get("successful_agent_ids", []),
        "failed": reply.get("unsuccessful_agent_ids", [])
    }

# === USAGE EXAMPLE ===
triage_result = handle_triage(
    agent_ids=["REAL_AGENT_ID"],  # Replace with actual agent ID
    collector_uuid="REAL_COLLECTOR_UUID"  # Replace with actual collector UUID
)

if triage_result:
    if "error" in triage_result:
        print(f"❌ Error: {triage_result['error']}")
        if "raw" in triage_result:
            print(f"🔍 Raw response: {triage_result['raw']}")
    else:
        action_id = triage_result["action_id"]
        success = triage_result["success"]
        failed = triage_result["failed"]

        if success:
            print(f"✅ Triage action {action_id} succeeded for: {success}")
        if failed:
            print(f"❌ Triage action {action_id} failed for: {failed}")
else:
    print("⚠️ Triage request failed or returned no data.")
