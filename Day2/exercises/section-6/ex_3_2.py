from pydantic import BaseModel, Field

class User(BaseModel):
    id: int = Field(..., alias="user_id")
    name: str

# Example usage
user_data = {"user_id": 123, "name": "Shreyas"}
user = User(**user_data)
print(user)

