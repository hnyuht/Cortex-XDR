import requests

def test_connection(urls):
    results = {}
    headers = {"User-Agent": "Mozilla/5.0 (compatible; TestScript/1.0)"}

    for url in urls:
        print(f"Testing connection to: {url}")  # Inform the user about progress
        try:
            response = requests.get(f"https://{url}", headers=headers, timeout=5)
            if response.status_code == 200:
                results[url] = "Pass"
            else:
                results[url] = f"Fail (HTTP {response.status_code})"
        except requests.exceptions.ConnectionError:
            results[url] = "Fail (Connection error)"
        except requests.exceptions.Timeout:
            results[url] = "Fail (Timeout)"
        except requests.exceptions.RequestException as e:
            results[url] = f"Fail ({str(e)})"
    
    return results


if __name__ == "__main__":
    # List of URLs to test
    urls = [
        "<xdr-tenant>.xdr.<region>.paloaltonetworks.com",
        "distributions.traps.paloaltonetworks.com",
        "dc-<xdr-tenant>.traps.paloaltonetworks.com",
        "ch-<xdr-tenant>.traps.paloaltonetworks.com",
        "cc-<xdr-tenant>.traps.paloaltonetworks.com",
        "panw-xdr-installers-prod-us.storage.googleapis.com",
        "global-content-profiles-policy.storage.googleapis.com"
    ]
    
    print("Starting connectivity tests...\n")
    results = test_connection(urls)
    
    print("\nTest Results:")
    for url, status in results.items():
        print(f"{url} | {status}")
