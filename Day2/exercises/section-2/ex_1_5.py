import os

def read_file_lbyl(filename):
    if os.path.exists(filename):  # Checking before accessing
        with open(filename, 'r') as file:
            return file.read()
    else:
        return "File does not exist"

result = read_file_lbyl("somefile.txt")
print(result)
