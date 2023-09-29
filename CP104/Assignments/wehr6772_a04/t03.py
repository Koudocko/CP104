"""
-------------------------------------------------------
Returns te average of the two out of three largest numbers
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-12"
-------------------------------------------------------
"""

# Imports
from functions import largest_average

# Get the three values to compare
val1 = float(input("First value: "))
val2 = float(input("Second value: "))
val3 = float(input("Third value: "))

# Compute average of the two largest
average = largest_average(val1, val2, val3)

# Display AQI label
print(f"largest_average({val1}, {val2}, {val3}) -> {average}")
