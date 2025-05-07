def is_even(number):
    """Check if a number is even."""
    return number % 2 == 0

def can_vote(age):
    """Check if someone is eligible to vote."""
    return age >= 18

print(is_even(4))  # Output: True
print(can_vote(20))  # Output: True
