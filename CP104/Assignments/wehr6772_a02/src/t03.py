"""
-------------------------------------------------------
Reformat the date of YYYYMMDD as YYYY/MM/DD
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-12"
-------------------------------------------------------
"""

# Get date in YYMMDD format
date = int(input("Enter ad date in the format YYYYMMDD: "))

# Compute the year with integer division
year = date // 10000
# Remove the year from the date
remainder = date % 10000
# Compute the month with integer division
month = remainder // 100
# Remove the month from the date, leftover is day
day = remainder % 100

# Display the reformatted date
print(f"The reformatted date: {year}/{month:02d}/{day:02d}")
