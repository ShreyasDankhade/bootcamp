import time
from functools import lru_cache

# Without memoization
def uncached_fib(n):
    if n <= 1:
        return n
    return uncached_fib(n-1) + uncached_fib(n-2)

# With memoization
@lru_cache(maxsize=None)
def cached_fib(n):
    if n <= 1:
        return n
    return cached_fib(n-1) + cached_fib(n-2)

# Example usage to compare performance
start_time = time.time()
uncached_fib(35)
print("Uncached Fibonacci took", time.time() - start_time)

start_time = time.time()
cached_fib(35)
print("Cached Fibonacci took", time.time() - start_time)
