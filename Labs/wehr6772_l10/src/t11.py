"""
-------------------------------------------------------
Find the last longest word in words.txt
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-15"
-------------------------------------------------------
"""

# Imports
from functions import find_longest

print("file 'words.txt' open for reading")

# File handle
fh = open("words.txt", "r")

# Get and display last longest word
word = find_longest(fh)
print(f"'{word}' is the last longest word")

fh.close()
