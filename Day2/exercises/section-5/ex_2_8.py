from pathlib import Path

def check_file_existence(file_path):
    path = Path(file_path)
    return path.exists() and path.is_file()

print(check_file_existence("myfile.txt"))  # Output: True or False based on file existence
