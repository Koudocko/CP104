"""
-------------------------------------------------------
Counts the number of each type of character in addresses.txt.
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-12"
-------------------------------------------------------
"""

# Imports
from functions import file_statistics

# Open file handle to addresses.txt as read
file_handle = open("addresses.txt", "r", encoding="utf-8")

# Get count of each type of character in file
ucount, lcount, dcount, wcount, rcount = file_statistics(file_handle)

# Display all character counters
print(f"file_statistics(file_handle) -> {ucount}, {lcount}, {dcount}, {wcount}, {rcount}")

# Close file handle
file_handle.close()

