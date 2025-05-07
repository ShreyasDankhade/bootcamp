from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int
    country: str = "India"

user = User(name="Shreyas", age=25)
print(user)