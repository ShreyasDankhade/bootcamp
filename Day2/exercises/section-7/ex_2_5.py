import itertools

def first_n_lines(file_path, n):
    with open(file_path, 'r') as file:
        return itertools.islice(file, n)

for line in first_n_lines('large_file.txt', 10):
    print(line)
