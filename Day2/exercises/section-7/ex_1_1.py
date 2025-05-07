import timeit

def time_sum():
    return timeit.timeit("sum(range(10000))", number=1000)

execution_time = time_sum()
print(f"Execution time: {execution_time} seconds")
