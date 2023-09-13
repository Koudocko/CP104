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
from functions import get_indexes

# Get list of indexes matching target in list of numbers
index_list = get_indexes([5, 1, 8, 9, 5, 2, 5, 3], 5)

# Print the indexes of the matches
print(f"get_indexes([5, 1, 8, 9, 5, 2, 5, 3], 5) -> {index_list}")
