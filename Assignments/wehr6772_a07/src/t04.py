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
minuend = ["z", "y", "x", "w"]
init_minuend = minuend.copy();
subtrahend = ["a", "b", "c"]

# Subtract subtrahend list from minuend list
list_subtract(minuend, subtrahend)

# Display updated minuend list
print(f"list_subtract({init_minuend}, {subtrahend}) -> None")
print(f"  minuend after: {minuend}")
