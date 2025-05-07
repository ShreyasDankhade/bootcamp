class AlwaysExitContext:
    def __enter__(self):
        print("Entering the context")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting the context")
        if exc_type:
            print(f"An exception occurred: {exc_val}")
        return False


def ensure_cleanup():
    with AlwaysExitContext():
        print("Inside the context")
        raise Exception("Error occurred")


ensure_cleanup()
