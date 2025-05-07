from functools import wraps

def log_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Before calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"After calling {func.__name__}")
        return result
    return wrapper

@log_execution
def greet(name):
    """Greets the person."""
    return f"Hello, {name}"

print(greet("Shreyas"))  # Output: Before calling greet
                       #         After calling greet
                       #         Hello, Shreyas
