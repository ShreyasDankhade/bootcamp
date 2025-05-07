def calculate_total_price(cart_items):
    """Calculate the total price of the items in the shopping cart."""
    total = sum(item['price'] for item in cart_items)
    return total


cart = [{'price': 10}, {'price': 20}]
total = calculate_total_price(cart)
print(total)  # Output: 30
