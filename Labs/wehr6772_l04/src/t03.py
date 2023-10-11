"""
-------------------------------------------------------
Computes the area of a circle
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-15"
-------------------------------------------------------
"""

# Imports
from functions import area

# Get radius of circle
radius = float(input("Input radius: "))

# Compute area from radius
ar = area(radius)

# Display computed area
print(f"area({radius}) -> {ar}")
