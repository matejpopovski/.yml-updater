import os
import re

 

def rename_tests_in_file(file_path):
    """Read a YAML file, rename 'tests:' to 'data_tests:', and write the changes back."""
    with open(file_path, 'r') as file:
        content = file.readlines()

    new_content = []
    for line in content:
        # Check if the line contains 'tests:'
        if 'tests:' in line:
            # Replace 'tests:' with 'data_tests:' while preserving indentation
            new_line = re.sub(r'^(\s*)tests:', r'\1data_tests:', line)
            new_content.append(new_line)
        else:
            new_content.append(line

    with open(file_path, 'w') as file:
        file.writelines(new_content)

def process_yml_files(directory):
    """Iterate through files in the directory and process .yml files."""
    for filename in os.listdir(directory):
        if filename.endswith('.yml'):
            file_path = os.path.join(directory, filename)
            rename_tests_in_file(file_path)

if __name__ == '__main__':
    current_directory = os.getcwd()
    process_yml_files(current_directory)