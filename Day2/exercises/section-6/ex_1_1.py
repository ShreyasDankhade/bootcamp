from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int

user = User(name="Shreyas", age=30)
print(user)
