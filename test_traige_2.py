import requests

url = "https://api-yourfqdn/public_api/v1/get_triage_presets"

payload = {"request_data": {}}
headers = {
    "Authorization": "your_api_key",         # Replace with your actual API key
    "x-xdr-auth-id": "your_api_key_id",      # Replace with your actual API key ID
    "Content-Type": "application/json",
    "Accept": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

# Try to decode JSON safely
try:
    response.raise_for_status()
    print("Raw JSON Response:")
    print(response.json())
except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
    print(f"Status code: {response.status_code}")
    print("Response text:", response.text)
except requests.exceptions.RequestException as err:
    print(f"Request error: {err}")
except ValueError:
    print("Response is not valid JSON.")
    print("Raw response:")
    print(response.text)
