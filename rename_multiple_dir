import os
import re


def rename_tests_in_file(file_path):
    """Read a YAML file, rename 'tests:' to 'data_tests:', and write the changes back."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.readlines()
    except UnicodeDecodeError:
        # Handle files that are not encoded in UTF-8
        print(f"Warning: '{file_path}' is not encoded in UTF-8, skipping.")
        return

    new_content = []
    for line in content:
        # Check if the line contains 'tests:'
        if 'tests:' in line:
            # Replace 'tests:' with 'data_tests:' while preserving indentation
            new_line = re.sub(r'^(\s*)tests:', r'\1data_tests:', line)
            new_content.append(new_line)
        else:
            new_content.append(line)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(new_content)

def process_yml_files(directory):
    """Recursively iterate through directories and process .yml files."""
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith('.yml'):
                file_path = os.path.join(root, filename)
                rename_tests_in_file(file_path)

if __name__ == '__main__':
    current_directory = os.getcwd()
    process_yml_files(current_directory)