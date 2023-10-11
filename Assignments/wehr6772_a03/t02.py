"""
-------------------------------------------------------
Computes the time taken to cut a lawn
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-12"
-------------------------------------------------------
"""

# Imports
from functions import lawn_mow_time

# Get lawn dimensions and speed of mower
width = int(input("Width (m): "))
length = int(input("Length (m): "))
speed = int(input("Speed (m^2/minute): "))

# Compute time taken
time = lawn_mow_time(width, length, speed)

# Display low mow time
print(f"lawn_mow_time({width}, {length}, {speed}) -> {time}")
