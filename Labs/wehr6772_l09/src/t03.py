"""
-------------------------------------------------------
Splits a product code into sub strings
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-15"
-------------------------------------------------------
"""

# Imports
from functions import parse_code

# Get product code
product_code = input("Enter product code: ")

# Get product code parts
pc, pi, pq = parse_code(product_code)

# Display parsed components
print(f"parse_code({product_code}) -> ('{pc}', '{pi}', '{pq}')")
