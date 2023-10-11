"""
-------------------------------------------------------
Adds spaces between words in a string.
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-12"
-------------------------------------------------------
"""

# Imports
from functions import add_spaces

# Get sentence without spaces
sentence = input("Input sentence: ")

# Get new sentence with spaces
spaced = add_spaces(sentence)

# Print sentence with spaces
print(f"add_spaces({sentence}) -> {spaced}")
