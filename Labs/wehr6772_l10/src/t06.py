"""
-------------------------------------------------------
Display information about a set of numbers from numbers.txt
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-15"
-------------------------------------------------------
"""

# Imports
from functions import number_stats

# File handle
fh = open("numbers.txt", "r")

# Get statistics from set of numbers
smallest, largest, total, average = number_stats(fh)

# Display statistics
print(f"Smallest: {smallest}")
print(f"Largest: {largest}")
print(f"Total: {total}")
print(f"Average: {average}")

fh.close()
