from pydantic import BaseModel

class User(BaseModel):
    age: int

user_data = {"age": "42"}
user = User(**user_data)
print(user)