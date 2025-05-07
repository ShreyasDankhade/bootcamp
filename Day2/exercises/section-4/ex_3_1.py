from functools import partial

# Create a partial function where base=2 for int()
int_base_2 = partial(int, base=2)

print(int_base_2("1010"))  # Output: 10 (binary 1010 -> decimal 10)
