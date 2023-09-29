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

from functions import extract_date

# Get date number
date_number = int(input("Enter ad date in the format YYYYMMDD: "))

# Reformat date
year, month, day = extract_date(date_number)

# Display reformatted date
print(f"extract_date({date_number}) -> {year}, {month}, {day}")
