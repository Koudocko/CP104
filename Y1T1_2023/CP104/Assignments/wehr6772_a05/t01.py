"""
-------------------------------------------------------
Compute the factorial of a number
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-12"
-------------------------------------------------------
"""

# Imports
from functions import calc_factorial

# Get number for factorial
number = int(input("Enter number: "))

# Compute factorial
product = calc_factorial(number)

# Display factorial product
print(f"calc_factorial({number}) -> {product}")

