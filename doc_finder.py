import os

root_directory = 'C:\\'
extensions = ['.xlsx', '.doc', '.docx', '.pdf']
output_directory = 'C:\\temp\\XDR'
output_file = os.path.join(output_directory, 'file_list.txt')

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

with open(output_file, 'w') as f:
    for root, dirs, files in os.walk(root_directory):
        for file in files:
            if any(file.endswith(ext) for ext in extensions):
                file_path = os.path.join(root, file)
                f.write(file_path + '\n')
                print(file_path)
print('File list saved to:', output_file)
