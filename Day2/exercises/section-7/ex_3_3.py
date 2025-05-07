import traceback

def faulty_function():
    try:
        result = 1 / 0  # Will raise a ZeroDivisionError
    except Exception:
        print(traceback.format_exc())

faulty_function()
