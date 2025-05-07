MAX_RETRIES = 3

def retry_operation():
    attempt = 0
    while attempt < MAX_RETRIES:
        try:
            # Simulate operation
            print("Trying operation...")
            # operation success
            return True
        except Exception as e:
            print(f"Error: {e}, retrying...")
            attempt += 1
    return False


success = retry_operation()
print(success)