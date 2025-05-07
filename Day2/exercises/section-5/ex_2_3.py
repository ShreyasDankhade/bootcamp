from pathlib import Path

def write_to_file(file_path, content):
    Path(file_path).write_text(content)

write_to_file("output.txt", "hello")
