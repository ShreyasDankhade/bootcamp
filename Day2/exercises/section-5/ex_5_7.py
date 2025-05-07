import concurrent.futures

def compute_square(number):
    return number ** 2

def parallel_computation():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(compute_square, [1, 2, 3, 4, 5])
    return list(results)

results = parallel_computation()
print(results)