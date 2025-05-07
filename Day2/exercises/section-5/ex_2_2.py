from pathlib import Path

def list_python_files(directory):
    return list(Path(directory).glob("*.py"))

python_files = list_python_files(".")
print(python_files)
