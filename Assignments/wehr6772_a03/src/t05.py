"""
-------------------------------------------------------
Computes the distance an object fell from the time taken
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-15"
-------------------------------------------------------
"""

# Imports
from functions import falling_distance

# Get time it took for the object to fall
falling_time = int(input("Input time taken to fall: "))

# Compute distance object fell
distance = falling_distance(falling_time)

# Display distance object fell
print(f"falling_distance({falling_time}) -> {distance}")
