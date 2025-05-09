import os

def find_file(filename, search_path="/"):
    matches = []
    for root, dirs, files in os.walk(search_path):
        if filename in files:
            full_path = os.path.join(root, filename)
            matches.append(full_path)
    return matches

if __name__ == "__main__":
    search_filename = input("Enter the filename to search for: ").strip()
    start_path = input("Enter the starting path (default is '/'): ").strip() or "/"

    print(f"Searching for '{search_filename}' in '{start_path}'...\n")
    results = find_file(search_filename, start_path)

    if results:
        print("Found file(s):")
        for path in results:
            print(path)
    else:
        print("No files found.")
