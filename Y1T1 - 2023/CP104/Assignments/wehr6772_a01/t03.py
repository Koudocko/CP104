"""
-------------------------------------------------------
Convert the input miles to kilometers
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-12"
-------------------------------------------------------
"""

# Constants
CONVERSION_FACTOR = 1.61

# Get number of miles input
miles = float(input("Length in miles: "))

# Convert to kilometers with conversion factor
km = miles * CONVERSION_FACTOR

print(f"Length in km: {km}")
