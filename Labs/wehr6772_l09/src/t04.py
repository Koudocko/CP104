"""
-------------------------------------------------------
Validates a given product code's segments
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-15"
-------------------------------------------------------
"""

# Imports
from functions import validate_code

# Get product code
product_code = input("Enter product code: ")

# Call implemented validate_code function
category, digits, qualifiers = validate_code(product_code)

# Display validation of product code
print(f"validate_code({product_code}) -> ({category}, {digits}, {qualifiers})")
