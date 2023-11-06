"""
-------------------------------------------------------
Returns all instances of the minimum value in a list
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-15"
-------------------------------------------------------
"""

# Imports
from functions import min_search

# List to be searched for min value
values = [-1, 0, 1, 2, 3, 4, 5, -1]

# Get indexes of the min value occurences
indexes = min_search(values)

# Display indexes of min values
print(f"min_search({values}) -> {indexes}")
