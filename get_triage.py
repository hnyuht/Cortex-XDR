import requests

# === CONFIGURATION ===
url = "https://api-yourtenant.xdr.us.paloaltonetworks.com/public_api/v1/get_triage_presets"  # Replace with actual URL
api_key_id = "YOUR_API_ID"  # Replace with your actual API ID
api_key = "YOUR_API_KEY"  # Replace with your actual API Key

# === PAYLOAD AND HEADERS ===
payload = { "request_data": {} }
headers = {
    "Authorization": api_key,
    "x-xdr-auth-id": api_key_id,
    "Content-Type": "application/json",
    "Accept": "application/json"
}

# === MAKE THE API REQUEST ===
try:
    response = requests.post(url, json=payload, headers=headers)
    
    # Check the HTTP status code for better error reporting
    print(f"HTTP Status Code: {response.status_code}")
    
    # If the status code isn't in the 200 range, raise an exception
    response.raise_for_status()

    # Try to parse the JSON response
    try:
        result = response.json()
        print(result)
    except ValueError:
        # If it fails to parse as JSON, print the raw response and handle it
        print("❌ Error: Response not in JSON format. Here's the raw response:")
        print(response.text)

except requests.exceptions.RequestException as e:
    # If the request fails (due to network issues, invalid URL, etc.)
    print(f"❌ Request failed: {e}")
    if hasattr(response, 'status_code'):
        print(f"HTTP Status Code: {response.status_code}")  # Print status code in case of error
    if hasattr(response, 'text'):
        print(f"Raw Response: {response.text}")  # Print raw HTML response in case of failure
