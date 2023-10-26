"""
-------------------------------------------------------
Total number of hours IAs work over the weeks
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-15"
-------------------------------------------------------
"""

# Imports
from functions import ia_hours

# Get number of IAs
ia_count = int(input("Input number of IAs: "))

# Compute total number of hours worked by IAs
total_hours = ia_hours(ia_count)
print(f"ia_hours({ia_count}) -> {total_hours}")
