"""
-------------------------------------------------------
Subtracts list of targets from another list.
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-12"
-------------------------------------------------------
"""

# Imports
from functions import list_subtract

# Initialize arguments
minuend = [5, 5, 4, 5]
subtrahend = [5]

# Subtract subtrahend list from minuend list
list_subtract(minuend, subtrahend)

# Display updated minuend list
print(f"list_subtract([5, 5, 4, 5], [5]) -> None")
print(f"  minuend after: {minuend}")
