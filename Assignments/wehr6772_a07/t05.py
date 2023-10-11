"""
-------------------------------------------------------
Validates that a list of numbers is sorted.
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-12"
-------------------------------------------------------
"""

# Imports
from functions import verify_sorted

# Initialize numbers list
numbers = [1, 2, 3]

# Validate that numbers list is sorted
in_order, index = verify_sorted(numbers)

# Display output of verification
print(f"verify_sorted({numbers}) -> {in_order}, {index}")
