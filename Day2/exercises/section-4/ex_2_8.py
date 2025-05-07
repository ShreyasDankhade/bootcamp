def custom_logger(message):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"{message} Before calling {func.__name__}")
            result = func(*args, **kwargs)
            print(f"{message} After calling {func.__name__}")
            return result
        return wrapper
    return decorator

# Example usage
@custom_logger("Log message")
def greet(name):
    return f"Hello, {name}"

print(greet("Shreyas"))
