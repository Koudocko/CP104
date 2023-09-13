"""
-------------------------------------------------------
Combines two colours into another
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-12"
-------------------------------------------------------
"""

# Imports
from functions import colour_combine

# Get the two colours to be mixed
rgb_colour1 = input("First colour: ")
rgb_colour2 = input("Second colour: ")

# Obtain new mixed colour
rgb_colour = colour_combine(rgb_colour1, rgb_colour2)

# Display the mixed colour
print(f"colour_combine({rgb_colour1}, {rgb_colour2}) -> {rgb_colour}")
