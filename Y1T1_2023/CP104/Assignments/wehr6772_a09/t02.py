"""
-------------------------------------------------------
Display integers list from numbers.txt.
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-12"
-------------------------------------------------------
"""

# Imports
from functions import read_integers

# Open file handle to numbers.txt as read
file_handle = open("numbers.txt", "r", encoding="utf-8")

# Get list of numbers from file
number_list = read_integers(file_handle)

# Display list of numbers 
print(f"read_integers(file_handle) -> {number_list}")

# Close file handle
file_handle.close()
