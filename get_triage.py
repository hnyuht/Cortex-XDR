import json
import requests

# Updated URL and API details
url = "https://api-yourfqdn/public_api/v1/get_risky_users"  # Replace with your endpoint

headers = {
    "Authorization": "API KEY",  # Replace with your API key
    "x-xdr-auth-id": "API ID",  # Replace with your API ID
    "Content-Type": "application/json",
    "Accept": "application/json"
}

# No payload needed for this endpoint, but you can pass empty or specific data if needed
payload = {}

try:
    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()  # Raise exception for bad response status
    res_json = response.json()

    if res_json and 'reply' in res_json:
        top_users = res_json['reply'][:10]  # Get top 10 users
        for user in top_users:
            print(f"User ID: {user['id']}, Score: {user['score']}")
    else:
        print("No response or 'reply' key not found in response.")
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
except ValueError as e:
    print(f"Failed to parse response JSON: {e}")
