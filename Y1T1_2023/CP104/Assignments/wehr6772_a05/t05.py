"""
-------------------------------------------------------
Sums a number of values from a start, incrementing by some each time.
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-12"
-------------------------------------------------------
"""

# Imports
from functions import range_addition

# Get start, incrememnt, and count numbers
start = int(input("Start number: "))
increment = int(input("Increment amount: "))
count = int(input("Count number: "))

# Get addition total
total = range_addition(start, increment, count)

# Print addition output total
print(f"range_addition({start}, {increment}, {count}) -> {total}")
