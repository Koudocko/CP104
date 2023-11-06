"""
-------------------------------------------------------
Retrieves indexes for value matches in a list
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-15"
-------------------------------------------------------
"""

# Imports
from functions import many_search

# List and target
values = [94, 96, -22, -79, -28, 96, -50, 71, 24, -32]
value = 96

# Get indexes of target in list
indexes = many_search(values, value)

# Display indexes of match
print(f"many_search({values}, {value}) -> {indexes}")
