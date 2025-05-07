import time

def measure_execution_time(func):
    start_time = time.time()
    result = func()
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time

def slow_function():
    total = 0
    for i in range(1000000):
        total += i
    return total

result, execution_time = measure_execution_time(slow_function)
print(f"Execution time: {execution_time} seconds")
