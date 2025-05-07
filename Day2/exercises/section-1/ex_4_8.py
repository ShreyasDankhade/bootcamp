def scope_error():
    print(x)  # Trying to access 'x' before it is assigned
    x = 10

try:
    scope_error()
except UnboundLocalError as e:
    print(f"Error: {e}")  # Output: Error: local variable 'x' referenced before assignment
