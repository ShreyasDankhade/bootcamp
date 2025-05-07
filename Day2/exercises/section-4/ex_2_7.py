import time

def retry(retries=3):
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempt = 0
            while attempt < retries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempt + 1} failed: {e}")
                    attempt += 1
                    if attempt == retries:
                        raise
                    time.sleep(1)
        return wrapper
    return decorator

# Example usage
@retry(retries=2)
def fail_function():
    raise ValueError("Something went wrong")

try:
    fail_function()
except ValueError as e:
    print("Failed after retrying:", e)
