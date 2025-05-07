class Greeter:
    def __init__(self, greeting="Hello"):
        self.greeting = greeting

    def __call__(self, name):
        return f"{self.greeting}, {name}!"

# Example usage
greeter = Greeter("Hi")
print(greeter("Shreyas"))
