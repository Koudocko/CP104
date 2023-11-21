"""
-------------------------------------------------------
Fetches the frequency of a word occuring in words.txt
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-15"
-------------------------------------------------------
"""

# Imports
from functions import count_frequency_word

print("file 'words.txt' open for reading")

# Get word target to count
word = input("Word to count: ")

# File handle
fh = open("words.txt", "r")

# Get and display frequency of target in file
count = count_frequency_word(fh, word)
print(f"'{word}' appears {count} time(s)")

fh.close()
