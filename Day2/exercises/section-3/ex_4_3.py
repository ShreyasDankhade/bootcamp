from dataclasses import dataclass

@dataclass(frozen=True)
class User:
    name: str
    age: int

user = User("Shreyas", 30)
print(user)

# Uncommenting the line below will raise a FrozenInstanceError
user.age = 35
# Error: cannot assign to field 'age'
