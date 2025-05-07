"""
This module contains functions for calculating discounts and handling purchases.
"""

def get_discount(price, discount_percentage):
    """Calculate the discount on a given price."""
    return price * (discount_percentage / 100)
