from dataclasses import dataclass

@dataclass(slots=True)
class User:
    name: str
    age: int
    country: str = "India"

# Example usage
user = User(name="Shreyas", age=26)
print(user)