strings = ["hi", "hello", "bye"]

# Filter even-length strings
even_length_strings = [string for string in strings if len(string) % 2 == 0]
print(even_length_strings)  # ['hello']
