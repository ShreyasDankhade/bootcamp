import tempfile

def create_temp_file():
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(b"Temporary content.")
        return temp_file.name

temp_file_name = create_temp_file()
print(f"Temporary file created: {temp_file_name}")
