"""
-------------------------------------------------------
Extracts attributes from a date in the format YYYYMMDD
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-15"
-------------------------------------------------------
"""

# Imports
from functions import extract_date

# Get formatted date
date_number = int(input("Enter a date in the format YYYYMMDD: "))

# Extract year, month, and day attributes from date
year, month, day = extract_date(date_number)

# Display extracted attributes
print(f"extract_date({date_number}) -> {year}, {month}, {day}")
