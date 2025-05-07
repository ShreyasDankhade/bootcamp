def divide(a, b):
    try:
        return a / b
    except Exception as e:
        print(type(e), e)  # Print exception type and message
        return None

result = divide(10, 0)
