"""
-------------------------------------------------------
Determines which quadrant a coordinate falls under
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-15"
-------------------------------------------------------
"""

# Imports
from functions import quadrant

# Get x and y coords of point
x = int(input("Input x coordinate: "))
y = int(input("Input y coordinate: "))

# Get quadrant associated with coordinates
location = quadrant(x, y)

# Display quadrant location of coordinates
print(f"quadrant({x}, {y}) -> {location}")
