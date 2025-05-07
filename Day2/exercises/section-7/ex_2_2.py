import sys

def create_large_list():
    return [x * x for x in range(1000000)]

def create_large_generator():
    return (x * x for x in range(1000000))

# Example usage
lst = create_large_list()
gen = create_large_generator()

print(f"List memory size: {sys.getsizeof(lst)} bytes")
print(f"Generator memory size: {sys.getsizeof(gen)} bytes")
