#!/usr/bin/env python3

import json
import requests
import re

# NOTES: PLEASE CHECK URL
base_url = "https://api-[REMOVE BRACKETS TENANT URL].xdr.us.paloaltonetworks.com/public_api/v1/alerts/"
api_key_id = "INSERT ID"
api_key = "INSERT API KEY"

def make_request(endpoint, payload=None):
	url = base_url + endpoint
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
# Request all alerts
req_body = {
	"request_data": {}
}
# Make the request to get all alerts
response = make_request("get_alerts/", req_body)
# Print the entire response for debugging
print("Full response:")
print(json.dumps(response, indent=4))

# Filter alerts based on resolution_status and resolution_comment
filtered_alerts = [alert for alert in response.get("reply", {}).get("data", []) if
					alert.get("status", "").lower() == "new" and
					"duplicate" in str(alert.get("resolution_comment", "")).lower() and
					(alert.get("deduplicate_token") is not None and alert.get("deduplicate_token") != "null")]
# Print the alerts that match the filter
for alert in filtered_alerts:
	alert_id = alert.get("alert_id", "N/A")
	resolution_status = alert.get("status", "N/A")
	resolution_comment = alert.get("resolution_comment", "N/A")
	print(f"Alert_ID: {alert_id} Resolution Status: {resolution_status} Resolution Comment: {resolution_comment}")
