"""
-------------------------------------------------------
Describes the wind speed based off the quantitative km/h
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-15"
-------------------------------------------------------
"""

# Imports
from functions import wind_speed

# Get wind speed
speed = int(input("Input wind speed: "))

# Associate category with wind speed
category = wind_speed(speed)

# Display category of wind speed
print(f"wind_speed({speed}) -> {category}")
