"""
-------------------------------------------------------
Find nearest power of two greater than or equal to target
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-15"
-------------------------------------------------------
"""

# Imports
from functions import power_of_two

# Get target
target = int(input("Enter power of two target: "))

# Compute closest power of two to target
power = power_of_two(target)

# Display power
print(power)
