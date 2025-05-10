import os

# === Change this to the filename you're searching for ===
TARGET_FILENAME = "example.txt"

def find_file(filename, search_path="/"):
    matches = []
    for root, dirs, files in os.walk(search_path, topdown=True):
        # Skip directories without permission
        try:
            if filename in files:
                matches.append(os.path.join(root, filename))
        except (PermissionError, FileNotFoundError):
            continue
    return matches

if __name__ == "__main__":
    print(f"Searching for '{TARGET_FILENAME}' from root '/'...\n")
    results = find_file(TARGET_FILENAME)

    if results:
        print("Found file(s):")
        for path in results:
            print(path)
    else:
        print("No files found.")
