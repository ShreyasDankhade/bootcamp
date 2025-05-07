import warnings

def divide(a, b):
    if b == 0:
        warnings.warn("Division by zero, result will be inf.")
        return float('inf')
    return a / b

result = divide(10, 0)
