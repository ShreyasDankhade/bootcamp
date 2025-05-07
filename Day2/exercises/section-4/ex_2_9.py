def validate_args(func):
    def wrapper(self, *args, **kwargs):
        if len(args) < 2:  # Validate that at least 2 arguments are passed
            raise ValueError("Insufficient arguments!")
        return func(self, *args, **kwargs)
    return wrapper

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @validate_args
    def update_info(self, name, age):
        self.name = name
        self.age = age
        return f"Updated info: {self.name}, {self.age}"

user = User("Shreyas", 25)
print(user.update_info("Neel", 30))  # Works fine
try:
    print(user.update_info("Suyog"))  # Raises ValueError
except ValueError as e:
    print(e)
