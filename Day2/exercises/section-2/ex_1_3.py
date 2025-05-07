def read_file_eafp(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "File not found"

# Example usage:
result = read_file_eafp("non_existent_file.txt")
print(result)  # Output: File not found
