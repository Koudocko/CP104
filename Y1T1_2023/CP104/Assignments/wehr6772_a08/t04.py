"""
-------------------------------------------------------
Determine if an ISBN is valid.
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-12"
-------------------------------------------------------
"""

# Imports
from functions import valid_isbn

# Get ISBN
isbn = input("Input ISBN: ")

# Get if ISBN is valid
is_valid = valid_isbn(isbn)

# Display output of ISBN validity
print(f"valid_isbn('{isbn}') -> {is_valid}")
