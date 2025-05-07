from contextlib import suppress

def suppress_file_not_found(file_path):
    with suppress(FileNotFoundError):
        with open(file_path, 'r') as f:
            return f.read()

content = suppress_file_not_found("non_existent_file.txt")
print(content)  # Output: None
