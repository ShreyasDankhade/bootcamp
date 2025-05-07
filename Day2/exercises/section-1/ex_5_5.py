class InvalidAgeError(Exception):
    """Custom exception for invalid age."""
    pass

def check_age(age):
    if age < 0:
        raise InvalidAgeError("Age cannot be negative")
    else:
        print(f"Valid age: {age}")

# Test the function
try:
    check_age(-5)
except InvalidAgeError as e:
    print(f"Error: {e}")  # Output: Error: Age cannot be negative
