from pathlib import Path

def read_file(file_path):
    return Path(file_path).read_text()

file_content = read_file("myfile.txt")
print(file_content)
