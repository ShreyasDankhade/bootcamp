from contextlib import suppress


def suppress_key_error():
    my_dict = {"name": "Alice"}

    # Using suppress to ignore KeyError
    with suppress(KeyError):
        print(my_dict["age"])  # This will not raise an error

    print("No error occurred.")


# Test the function
suppress_key_error()  # Output: No error occurred.
