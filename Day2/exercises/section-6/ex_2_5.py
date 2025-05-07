from pydantic import BaseModel, validator

class User(BaseModel):
    name: str
    age: int

    @validator("name")
    def capitalize_name(cls, v):
        return v.capitalize()

# Example usage
user_data = {"name": "Shreyas", "age": 25}
user = User(**user_data)
print(user)