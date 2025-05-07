def outer():
    message = "Hello from the outer function!"

    def inner():
        print(message)  # Accesses 'message' from the outer function

    inner()  # Calling the inner function


outer()  # Output: Hello from the outer function!
