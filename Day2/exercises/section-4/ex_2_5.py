def debug_info(func):
    def wrapper(*args, **kwargs):
        print(f"Function {func.__name__} called with arguments: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} returned: {result}")
        return result
    return wrapper

@debug_info
def add(a, b):
    return a + b

add(2, 3)
