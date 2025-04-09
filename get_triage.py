import requests

# === CONFIGURATION ===
url = "https://api-yourfqdn/public_api/v1/get_triage_presets"  # Replace with actual URL
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
    
    # Check if request was successful
    response.raise_for_status()

    # Try to parse the JSON response
    try:
        result = response.json()
        print(result)
    except ValueError:
        print("Error: Response not in JSON format. Raw response:")
        print(response.text)

except requests.exceptions.RequestException as e:
    print(f"❌ Request failed: {e}")
