def simple_logger(func):
    def wrapper(*args, **kwargs):
        print("Function started")
        result = func(*args, **kwargs)
        print("Function ended")
        return result
    return wrapper

@simple_logger
def say_hello(name):
    return f"Hello, {name}"

print(say_hello("Shreyas"))
