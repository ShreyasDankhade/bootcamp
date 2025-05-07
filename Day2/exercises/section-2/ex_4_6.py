import tempfile

def write_read_tempfile():
    with tempfile.TemporaryFile(mode='w+t') as tmp:
        tmp.write("Hello, temporary world!")
        tmp.seek(0)
        return tmp.read()

content = write_read_tempfile()
print(content)