"""
-------------------------------------------------------
Computes the slope of a line based on two end point coordinates
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-15"
-------------------------------------------------------
"""

# Imports
from functions import slope

# Get coordinates of two points
x1 = int(input("Input first x coordinate: "))
y1 = int(input("Input first y coordinate: "))
x2 = int(input("Input second x coordinate: "))
y2 = int(input("Input second y coordinate: "))

# Compute the slope of the line between the two points
slp = slope(x1, y1, x2, y2)

# Display the slope of the line
print(f"slope({x1}, {y1}, {x2}, {y2}) -> {slp}")
