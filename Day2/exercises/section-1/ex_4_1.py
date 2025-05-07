x = 10  # Global variable

def test_scope():
    x = 20  # Local variable
    print(f"Local x: {x}")

test_scope()  # Output: Local x: 20
print(f"Global x: {x}")  # Output: Global x: 10
