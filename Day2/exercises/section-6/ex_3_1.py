from pydantic import BaseModel, Field

class User(BaseModel):
    name: str
    email: str = Field(..., description="User's email address")

# Example usage
user_data = {"name": "Shreyas", "email": "alice@example.com"}
user = User(**user_data)
print(user)