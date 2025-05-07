def read_two_files(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        return f1.read(), f2.read()

content1, content2 = read_two_files("file1.txt", "file2.txt")
print(content1, content2)
