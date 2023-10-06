"""
-------------------------------------------------------
Converts celsius to fahrenheight
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-15"
-------------------------------------------------------
"""

# Imports
from functions import f_to_c

# Get temperature in fahrenheight
fahrenheight = int(input("Input temperature (F): "))

# Call implemented f_to_c function
celsius = f_to_c(fahrenheight)

# Display fahrenheight to celsius conversion
print(f"f_to_c({fahrenheight}) -> {celsius}")
