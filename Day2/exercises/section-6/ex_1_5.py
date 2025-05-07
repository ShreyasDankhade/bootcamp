from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int
    country: str = "India"

    def is_adult(self):
        return self.age >= 18


user = User(name="Eva", age=17)
print(user.is_adult())  # Output: False

adult_user = User(name="Frank", age=30)
print(adult_user.is_adult())  # Output: True
