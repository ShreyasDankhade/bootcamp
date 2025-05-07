from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int


user = User("Shreyas", 30)
print(user)  # Output: User(name='Shreyas', age=30)
