def apply_discount(price, discount_percentage):
    """
    Apply discount and return the final price.
    The discount is calculated by multiplying the price by the discount percentage.
    """
    # Calculate the discount
    discount = price * (discount_percentage / 100)

    # Subtract discount from price to get final price
    return price - discount
