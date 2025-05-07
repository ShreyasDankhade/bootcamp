import shutil
from pathlib import Path

def copy_file(src, dst):
    shutil.copy(src, dst)

copy_file("source.txt", "destination.txt")
