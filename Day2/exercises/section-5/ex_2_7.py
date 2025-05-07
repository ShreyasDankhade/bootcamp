from pathlib import Path

def show_absolute_path(file_path):
    return Path(file_path).resolve()

absolute_path = show_absolute_path("myfile.txt")
print(absolute_path)
