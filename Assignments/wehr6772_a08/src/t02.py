"""
-------------------------------------------------------
Convert a singular string to a plural one.
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-15"
-------------------------------------------------------
"""

# Imports
from functions import pluralize

# Get singular string 
string = input("Input singular string: ")

# Pluralize the singular string
pluralized = pluralize(string)

# Print the plural string
print(f"pluralize('{string}') -> {pluralized}")
