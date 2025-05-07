def catch_and_reraise(a, b):
    try:
        result = a / b
    except ZeroDivisionError as e:
        print(f"Logging error: {e}")
        raise  # Re-raises the exception

# Test the function
try:
    catch_and_reraise(10, 0)
except ZeroDivisionError as e:
    print(f"Handled error: {e}")  # Output: Logging error: division by zero
                                  # Output: Handled error: division by zero
