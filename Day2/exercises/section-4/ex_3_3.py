from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def say_hello(name):
    """Greets the person with the given name."""
    return f"Hello, {name}"

print(say_hello.__name__)  # Output: say_hello
print(say_hello.__doc__)  # Output: Greets the person with the given name.
