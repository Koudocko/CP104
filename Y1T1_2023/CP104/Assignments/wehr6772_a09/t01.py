"""
-------------------------------------------------------
Display some number of lines from students.txt.
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-12"
-------------------------------------------------------
"""

# Imports
from functions import file_top

# Open file handle to students.txt as read
file_handle = open("students.txt", "r", encoding="utf-8")

# Get count
count = int(input("Input count: "))

# Display lines from file
file_top(file_handle, count)

# Close file handle
file_handle.close()
