import os
import socket
import time
import subprocess

# Define the folder to scan
folder_to_scan = ["C:\\Windows\\Temp", "C:\\Temp"]

# Define the output file path
output_folder = "C:\\Temp\\CortexXDR"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
output_file = os.path.join(output_folder, f"{socket.gethostname()}_output.txt")

# Define the headers for the output file
headers = ["Path", "Filename", "File Creation", "File Size"]

# Open the output file
with open(output_file, "w") as f:
    # Write the headers to the file
    f.write("|".join(headers) + "\n")

    # Initialize the total size variable
    total_size = 0

    # Loop through each folder and subfolder
    for folder in folder_to_scan:
        for dirpath, dirnames, filenames in os.walk(folder):
            for filename in filenames:
                # Get the full path to the file
                file_path = os.path.join(dirpath, filename)

                # Get the file creation time
                file_creation_time = os.path.getctime(file_path)
                file_creation_time = time.strftime("%Y-%m-%d %I:%M:%S %p", time.localtime(file_creation_time))

                # Get the file size in bytes
                file_size = os.path.getsize(file_path)

                # Convert the file size to a human-readable format
                size_suffixes = ["B", "KB", "MB", "GB", "TB"]
                size_suffix_index = 0
                while file_size > 1024 and size_suffix_index < len(size_suffixes) - 1:
                    file_size /= 1024.0
                    size_suffix_index += 1
                file_size = "{:.2f} {}".format(file_size, size_suffixes[size_suffix_index])

                # Add the file size to the total size
                total_size += os.path.getsize(file_path)

                # Write the file details to the output file
                f.write("|".join([dirpath, filename, file_creation_time, file_size]) + "\n")

    # Convert the total size to a human-readable format
    size_suffix_index = 0
    while total_size > 1024 and size_suffix_index < len(size_suffixes) - 1:
        total_size /= 1024.0
        size_suffix_index += 1
    total_size = "{:.2f} {}".format(total_size, size_suffixes[size_suffix_index])

    # Write the total size to the output file
    f.write(f"\nTotal Size: {total_size}")

# Close the console window
subprocess.call('cmd /c exit /b', shell=True)
