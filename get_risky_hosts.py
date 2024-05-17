import json
import requests

# NOTES: PLEASE CHECK URL
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

# Get risk score
response = make_request("get_risky_hosts")

# Display only top 10 users with id and score
if response and 'reply' in response:
	top_users = response['reply'][:10]  # Get top 10 users
	for user in top_users:
		print(f"User ID: {user['id']}, Score: {user['score']}")
else:
	print("No response or 'reply' key not found in response.")
