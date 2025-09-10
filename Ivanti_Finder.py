import subprocess
import os
import sys

def import_cert(cert_path: str, store: str):
    """
    Import a certificate into a Windows cert store using certutil.
    cert_path: Path to .crt or .cer file
    store: Store name (Root = Trusted Root, CA = Intermediate)
    """
    if not os.path.exists(cert_path):
        print(f"[!] Certificate file not found: {cert_path}")
        return False

    try:
        subprocess.run(
            ["certutil", "-addstore", store, cert_path],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        print(f"[+] Imported {cert_path} into {store}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"[!] Failed to import {cert_path} into {store}: {e.stderr.decode()}")
        return False


def verify_cert(thumbprint: str, store: str):
    """
    Verify if a certificate with given thumbprint exists in a cert store.
    """
    try:
        result = subprocess.run(
            ["certutil", "-store", store],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        output = result.stdout.decode(errors="ignore").replace(" ", "").upper()
        thumbprint = thumbprint.replace(" ", "").upper()
        if thumbprint in output:
            print(f"[✓] Certificate {thumbprint} is installed in {store}")
            return True
        else:
            print(f"[✗] Certificate {thumbprint} not found in {store}")
            return False
    except subprocess.CalledProcessError as e:
        print(f"[!] Error verifying certificate in {store}: {e.stderr.decode()}")
        return False


if __name__ == "__main__":
    # Paths to DigiCert certificates (replace with actual paths or download them first)
    digicert_root = r"C:\temp\DigiCertTrustedRootG4.crt"
    digicert_intermediate = r"C:\temp\DigiCertTrustedG4CodeSigningRSA4096SHA3842021CA1.crt"

    # Import Root cert
    import_cert(digicert_root, "Root")

    # Import Intermediate cert
    import_cert(digicert_intermediate, "CA")

    # Example verification (replace with actual thumbprints)
    verify_cert("646C6EEB6A5BD4EED35B7E0CBCE43CEC49119746", "Root")
