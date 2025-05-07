# Save this in a script, e.g., profile_example.py
@profile
def slow_function():
    total = 0
    for i in range(1000000):
        total += i
    return total

# To run the profiling:
# $ kernprof -l -v profile_example.py
