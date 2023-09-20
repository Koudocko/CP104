"""
-------------------------------------------------------
Converts AQI reading to user friendly indicator
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-12"
-------------------------------------------------------
"""

# Imports
from functions import pollution_ranking

# Get AQI number
air_quality_index = int(input("Enter AQI: "))

# Convert AQI reading to label
pollution = pollution_ranking(air_quality_index)

# Display AQI label
print(f"pollution_ranking({air_quality_index}) -> {pollution}")
