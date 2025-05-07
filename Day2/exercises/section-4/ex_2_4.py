def memoize(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            print("Returning cached result")
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

@memoize
def add(a, b):
    return a + b

print(add(1, 2))  # Computed result
print(add(1, 2))  # Cached result
