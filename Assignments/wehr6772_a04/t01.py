"""
-------------------------------------------------------
Associates the day of the week with a number from 1-7
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-12"
-------------------------------------------------------
"""

# Imports
from functions import day_name

# Get day number
day_num = int(input("Please enter a number between 1 and 7: "))

# Convert day number to name
day = day_name(day_num)

# Display day name
print(f"day_of_the_week({day_num}) -> {day}")
