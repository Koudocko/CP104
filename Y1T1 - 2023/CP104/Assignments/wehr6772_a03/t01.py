"""
-------------------------------------------------------
Convert square footage to acres
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-12"
-------------------------------------------------------
"""

# Imports
from functions import footage_to_acres

square_footage = float(input("Square footage: "))
acres = footage_to_acres(square_footage)
print(f"footage_to_acres({square_footage}) -> {acres}")
