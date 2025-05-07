from memory_profiler import profile

@profile
def slow_function():
    total = 0
    for i in range(1000000):
        total += i
    return total

# to run use - python -m memory_profiler ex_1_8.py
