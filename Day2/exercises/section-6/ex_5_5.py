def is_valid_age(age):
    """Check if age is valid."""
    return age >= 18

def can_purchase_item(age, item):
    """Check if user can purchase an item based on their age and item price."""
    if not is_valid_age(age):
        return False
    if item['price'] > 1000:
        return False
    return True

item = {'name': 'Laptop', 'price': 1500}
result = can_purchase_item(20, item)
print(result)  # Output: False
