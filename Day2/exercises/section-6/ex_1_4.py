from dataclasses import dataclass

@dataclass(frozen=True)
class User:
    name: str
    age: int
    country: str = "India"

user = User(name="Shreyas", age=28)
try:
    user.age = 30  # This will raise an error
except FrozenInstanceError as e:
    print(e)  # Output: cannot assign to field 'age'
