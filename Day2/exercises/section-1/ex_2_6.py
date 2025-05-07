import sys

# List comprehension
list_comprehension = [x for x in range(1000000)]
print("List memory:", sys.getsizeof(list_comprehension))

# Generator expression
generator_expression = (x for x in range(1000000))
print("Generator memory:", sys.getsizeof(generator_expression))
