"""
-------------------------------------------------------
Convert square footage to acres
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-15"
-------------------------------------------------------
"""

# Imports
from functions import footage_to_acres

# Input the square footage
square_footage = float(input("Square footage: "))

# Convert square footage to acres
acres = footage_to_acres(square_footage)

# Display conversion in acres
print(f"footage_to_acres({square_footage}) -> {acres}")
