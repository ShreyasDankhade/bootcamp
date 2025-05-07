len = 5  # Shadowing the built-in len function

try:
    print(len([1, 2, 3]))  # Trying to use len() will raise a TypeError
except TypeError as e:
    print(f"Error: {e}")  # Output: Error: 'int' object is not callable
