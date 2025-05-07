import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function took {end_time - start_time} seconds to execute.")
        return result
    return wrapper


@timer
def slow_function():
    time.sleep(2)

slow_function()
