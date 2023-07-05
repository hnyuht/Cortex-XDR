import os
import subprocess
import re

# Full path to cleanmgr.exe
cleanmgr_path = r'C:\Windows\System32\cleanmgr.exe'

# Run Disk Cleanup and redirect the output to a text file
subprocess.run([cleanmgr_path, '/sagerun:1'], capture_output=True, text=True)

# Calculate the occupied space
total_size = 0

# Define the file categories and their corresponding paths
file_categories = {
    'Downloaded Program Files': r'C:\Windows\Downloaded Program Files',
    'Temporary Internet Files': r'C:\Users\%USERNAME%\AppData\Local\Microsoft\Windows\Temporary Internet Files',
    'Windows error reports and feedback': r'C:\ProgramData\Microsoft\Windows\WER',
    'DirectX shader cache': r'C:\Users\%USERNAME%\AppData\Local\Microsoft\DirectX Shader Cache',
    'Delivery Optimization Files': r'C:\Windows\SoftwareDistribution\DeliveryOptimization',
    'Recycle Bin': r'C:\$Recycle.Bin',
    'Temporary Files': r'C:\Windows\Temp',
    'Thumbnails': r'C:\Users\%USERNAME%\AppData\Local\Microsoft\Windows\Explorer'
}

# Traverse the file system and calculate size for each category
category_sizes = {}
for category, path in file_categories.items():
    expanded_path = os.path.expandvars(path)
    size = sum(
        sum(os.path.getsize(os.path.join(root, file)) for file in files)
        for root, dirs, files in os.walk(expanded_path, topdown=True, followlinks=False)
    )
    category_sizes[category] = size
    total_size += size

# Convert total size to a more readable format
def convert_size(size_in_bytes):
    units = ["bytes", "KB", "MB", "GB", "TB"]
    index = 0
    while size_in_bytes >= 1024 and index < len(units) - 1:
        size_in_bytes /= 1024
        index += 1
    return f"{size_in_bytes:.2f} {units[index]}"

# Convert total size to a readable format
total_size_readable = convert_size(total_size)

# Save the result to a text file in C:\temp\
file_path = r'C:\Temp\XDR\disk_cleanup_report.txt'
with open(file_path, 'w') as file:
    file.write("Occupied Space Breakdown:\n")
    for category, size in category_sizes.items():
        size_readable = convert_size(size)
        file.write(f"{category}: {size_readable}\n")
    file.write(f"\nTotal Occupied Space: {total_size_readable}\n")

print(f"Disk cleanup report saved to {file_path}")
