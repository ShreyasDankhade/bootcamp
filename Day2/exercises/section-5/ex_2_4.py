import os
import shutil
from pathlib import Path

def create_and_delete_dir():
    dir_path = Path("temp_dir")
    os.makedirs(dir_path, exist_ok=True)
    # Example of creating a file inside the directory
    (dir_path / "file.txt").write_text("This is a temporary file.")

    # Clean up the directory
    shutil.rmtree(dir_path)

create_and_delete_dir()
