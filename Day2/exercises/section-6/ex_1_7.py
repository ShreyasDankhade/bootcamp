from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int
    country: str = "India"

user1 = User(name="Shreyas", age=22)
user2 = User(name="Shreyas", age=22)
print(user1 == user2)