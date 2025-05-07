import logging

def divide(a, b):
    if b == 0:
        logging.error("Attempted division by zero.")
        raise ValueError("Division by zero is not allowed.")
    return a / b


try:
    result = divide(10, 0)
except ValueError as e:
    print(e)
