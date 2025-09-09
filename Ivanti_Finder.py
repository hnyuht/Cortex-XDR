import subprocess

def check_store(store_name: str) -> bool:
    try:
        result = subprocess.run(
            ["certutil", "-store", store_name],
            capture_output=True,
            text=True,
            check=True
        )
        return "DigiCert Trusted Root G4" in result.stdout
    except subprocess.CalledProcessError:
        return False

def main():
    if check_store("root") or check_store("user"):
        print("DigiCert Trusted Root G4 is INSTALLED on this system.")
    else:
        print("DigiCert Trusted Root G4 is NOT installed on this system.")

if __name__ == "__main__":
    main()
