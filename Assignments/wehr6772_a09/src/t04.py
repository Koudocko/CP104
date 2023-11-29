"""
-------------------------------------------------------
Adds line numbers to each line in wilde.txt.
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-15"
-------------------------------------------------------
"""

# Imports
from functions import line_numbering

# Open file handles to wilde.txt as read
fh_read = open("wilde.txt", "r", encoding="utf-8")
fh_write = open("wilde.txt", "r+", encoding="utf-8")

# Set line numbers in file
line_numbering(fh_read, fh_write)

# Close files handles
fh_read.close()
fh_write.close()

# Display the new file output
fh_review = open("wilde.txt", "r", encoding="utf-8") 
line = " "

while line != "":
    line = fh_review.readline()
    print(line, end="")

# Close file handle
fh_review.close()
