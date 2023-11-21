"""
-------------------------------------------------------
Copies contents of words.txt over to new_words.txt
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-15"
-------------------------------------------------------
"""

# Imports
from functions import file_copy

print("Copying 'words.txt' to 'new_words.txt'")

# File handles
fh_1 = open("words.txt", "r")
fh_2 = open("new_words.txt", "w")

# Copy file contents from word.txt to new_words.txt
file_copy(fh_1, fh_2)

fh_1.close()
fh_2.close()
