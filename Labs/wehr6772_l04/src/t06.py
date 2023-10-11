"""
-------------------------------------------------------
Computes various properties of a circle
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-15"
-------------------------------------------------------
"""

# Imports
from functions import pythag

# Get side lengths of triangle
s1 = float(input("Input side length 1: "))
s2 = float(input("Input side length 2: "))

# Compute propertise of circle
radius, diam, circ, area = pythag(s1, s2)

# Display properties of circle
print(f"pythag({s1}, {s2}) -> {radius}, {diam}, {circ}, {area}")
