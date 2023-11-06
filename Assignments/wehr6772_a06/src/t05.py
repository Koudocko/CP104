"""
-------------------------------------------------------
Determine the sum of factors of a number.
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-15"
-------------------------------------------------------
"""

# Imports
from functions import factor_summation

# Get input number
number = int(input("Input number: "))

# Compute sum of factors of number
total = factor_summation(number)

# Display total of all factors of number
print(f"factor_summation({number}) -> {total}")
