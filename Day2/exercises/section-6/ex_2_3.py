from pydantic import BaseModel

class Profile(BaseModel):
    bio: str
    location: str

class User(BaseModel):
    name: str
    age: int
    profile: Profile

# Example usage
user_data = {"name": "Shreyas", "age": 25, "profile": {"bio": "Developer", "location": "Wonderland"}}
user = User(**user_data)
print(user)