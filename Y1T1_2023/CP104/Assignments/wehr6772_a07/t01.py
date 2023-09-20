"""
-------------------------------------------------------
Obtains a list of all the factors of some number.
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-12"
-------------------------------------------------------
"""

# Imports
from functions import list_factors

# Get number to find factors from
number = int(input("Input number: "))

# Get list of factors of number
factors = list_factors(number)

# Display total wins from the teams
print(f"list_factors({number}) -> {factors}")
