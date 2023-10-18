"""
-------------------------------------------------------
Computes the time taken to cut a lawn
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-15"
-------------------------------------------------------
"""

# Imports
from functions import lawn_mow_time

# Get lawn dimensions and speed of mower
width = float(input("Width (m): "))
length = float(input("Length (m): "))
speed = float(input("Speed (m^2/minute): "))

# Compute time taken to mow lawn
time = lawn_mow_time(width, length, speed)

# Display lawn mow time
print(f"lawn_mow_time({width}, {length}, {speed}) -> {time}")
