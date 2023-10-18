"""
-------------------------------------------------------
Computes whether a number is evenly divisble by two others
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-15"
-------------------------------------------------------
"""

# Imports
from functions import is_divisible

n = int(input("Enter number to be divided: "))
i = int(input("Enter first number to divide: "))
j = int(input("Enter second number to divide: "))

# Get whether n is divisible
result = is_divisible(n, i, j)

# Display whether if n is divisbile by i and j
print(f"is_divisible({n}, {i}, {j}) -> {result}")
