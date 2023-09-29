"""
-------------------------------------------------------
Convert fahrenheight to celsius
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-15"
-------------------------------------------------------
"""

# Constants
# Water freezing temperature in fahrenheight
WATER_FREEZING_TEMP_F = 32

# Obtain temperature in fahrenheight
temperature_f = int(input("Temperature (F): "))

# Convert temperature from fahrenheight to celsius
temperature_c = int((temperature_f - 32) * 5/9)

# Display temperature in celsius
print(f"Temperature (C): {temperature_c}")
