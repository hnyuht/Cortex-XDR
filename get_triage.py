import requests

# Base URL and API credentials
base_url = "https://api-yourfqdn.xdr.us.paloaltonetworks.com/public_api/v1/"  # Replace with your actual base URL
api_key_id = "API ID"  # Replace with your actual API ID
api_key = "API KEY"    # Replace with your actual API KEY

# Function to make a request to the specified endpoint
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
        res.raise_for_status()  # Raise exception for bad response status
        return res.json()  # Return the parsed JSON response
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None
    except ValueError as e:
        print(f"Failed to parse response JSON: {e}")
        return None

# Request triage presets
response = make_request("get_triage_presets")  # Use the correct endpoint here

# Process the response and print the result
if response:
    print(response)  # Print the entire response if it exists
else:
    print("No response or error occurred.")
