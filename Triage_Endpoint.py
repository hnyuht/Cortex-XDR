import requests

# Base URL and API credentials
base_url = "https://api-yourfqdn/public_api/v1/"  # Replace with your actual base URL
api_key_id = ""  # Replace with your actual API ID
api_key = ""     # Replace with your actual API KEY

# Function to make a request to the triage endpoint
def make_request(payload):
    url = base_url + "triage_endpoint"
    headers = {
        "x-xdr-auth-id": str(api_key_id),
        "Authorization": api_key,
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    try:
        # Sending the request
        res = requests.post(url=url, headers=headers, json=payload)
        
        # Log status code and raw response text for debugging
        print("Status Code:", res.status_code)
        print("Raw Response:", res.text)
        
        res.raise_for_status()  # Raise exception for bad response status

        # Return the parsed JSON response
        return res.json()
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None
    except ValueError as e:
        print(f"Failed to parse response JSON: {e}")
        print(f"Response content: {res.text}")  # Print raw response content for debugging
        return None

# Payload data
payload = {
    "request_data": {
        "agent_ids": ["string"],  # Replace with actual agent IDs
        "collector_uuid": "string"  # Replace with actual collector UUID
    }
}

# Make the request to the triage endpoint
response = make_request(payload)

# Process the response and print the result
if response:
    print(response)
else:
    print("No response or error occurred.")
