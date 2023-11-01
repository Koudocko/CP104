"""
-------------------------------------------------------
Find nearest sum of squares greater than or equal to target
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-15"
-------------------------------------------------------
"""

# Imports
from functions import sum_squares

# Get target to approximate with sum of squares
target = int(input("Input target for sum of squares: "))

# Gets sum of squares closest to target
final = sum_squares(target)

# Display closest sum of squares
print(final)
