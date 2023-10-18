"""
-------------------------------------------------------
Computes whether a date is "magic" if the day times month equals year
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-15"
-------------------------------------------------------
"""

# Imports
from functions import magic_date

# Get date, day month year
day = int(input("Input day: "))
month = int(input("Input month: "))
year = int(input("Input year: "))

# Get whether date is magic
magic = magic_date(day, month, year)

print(f"magic_date({day}, {month}, {year}) -> {magic}")
