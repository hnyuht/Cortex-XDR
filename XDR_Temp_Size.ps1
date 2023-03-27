# Define the folder to scan
$folder_to_scan = "C:\Windows\Temp", "C:\Temp"

# Define the output file path
$output_folder = "C:\Temp\CortexXDR"
if (!(Test-Path $output_folder)) {
    New-Item -ItemType Directory -Path $output_folder | Out-Null
}
$output_file = Join-Path $output_folder "$env:COMPUTERNAME_output.txt"

# Define the headers for the output file
$headers = "Path", "Filename", "File Creation", "File Size"

# Initialize the total size variable
$total_size = 0

# Open the output file
Set-Content $output_file ("$($headers -join '|')`n")

# Loop through each folder and subfolder
foreach ($folder in $folder_to_scan) {
    Get-ChildItem -Path $folder -File -Recurse | ForEach-Object {
        # Get the full path to the file
        $file_path = $_.FullName

        # Get the file creation time
        $file_creation_time = $_.CreationTime.ToString("yyyy-MM-dd hh:mm:ss tt")

        # Get the file size in bytes
        $file_size = $_.Length

        # Convert the file size to a human-readable format
        $size_suffixes = "B", "KB", "MB", "GB", "TB"
        $size_suffix_index = 0
        while ($file_size -gt 1024 -and $size_suffix_index -lt ($size_suffixes.Length - 1)) {
            $file_size /= 1024.0
            $size_suffix_index += 1
        }
        $file_size = "{0:F2} {1}" -f $file_size, $size_suffixes[$size_suffix_index]

        # Add the file size to the total size
        $total_size += $_.Length

        # Write the file details to the output file
        Add-Content $output_file ("$($file_path -replace '\|','^|')|$file_creation_time|$file_size")
    }
}

# Convert the total size to a human-readable format
$size_suffix_index = 0
while ($total_size -gt 1024 -and $size_suffix_index -lt ($size_suffixes.Length - 1)) {
    $total_size /= 1024.0
    $size_suffix_index += 1
}
$total_size = "{0:F2} {1}" -f $total_size, $size_suffixes[$size_suffix_index]

# Write the total size to the output file
Add-Content $output_file ""
Add-Content $output_file "Total Size: $total_size"
