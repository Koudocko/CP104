"""
-------------------------------------------------------
Convert fahrenheight to celsius
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-09"
-------------------------------------------------------
"""

# Constants
WATER_FREEZING_TEMP_F = 32

# Obtain temperatures
temperature_f = int(input("Temperature (F): "))
temperature_c = int((temperature_f - 32) * 5/9)

print(f"Temperature (C): {temperature_c}")
