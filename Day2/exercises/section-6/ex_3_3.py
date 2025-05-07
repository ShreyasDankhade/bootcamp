from pydantic import BaseModel, Field

class User(BaseModel):
    id: int = Field(..., title="User ID", description="The unique identifier for the user", example=123)
    name: str = Field(..., title="User Name", description="The name of the user", example="Alice")

# Example usage
user_data = {"id": 123, "name": "Shreyas"}
user = User(**user_data)
print(user)