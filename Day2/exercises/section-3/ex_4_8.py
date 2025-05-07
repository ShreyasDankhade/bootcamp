from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int

@dataclass
class AdminUser(User):
    access_level: str

# Example usage:
admin = AdminUser("Shreyas", 30, "SuperAdmin")
print(admin)  # Output: AdminUser(name='Shreyas', age=30, access_level='SuperAdmin')
