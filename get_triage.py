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

    # Check if the status code is 200 OK
    if response.status_code == 200:
        try:
            # Attempt to parse the JSON response
            result = response.json()

            # Check if the "reply" and "triage_presets" keys exist in the response
            if "reply" in result and "triage_presets" in result["reply"]:
                print(result)  # Only print the JSON with "triage_presets"
            else:
                # Optionally handle case where the response doesn't contain the expected structure
                print("❌ Response does not contain the expected 'triage_presets' data.")
        except ValueError:
            # If the response is not valid JSON, we do nothing (silently ignore it)
            pass
    else:
        # If the response status code isn't 200, we print a message and exit
        print(f"❌ Received non-200 response: HTTP {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"❌ Request failed: {e}")
