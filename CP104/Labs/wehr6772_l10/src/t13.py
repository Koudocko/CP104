"""
-------------------------------------------------------
Copies contents of words.txt over to new_words.txt
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-09"
-------------------------------------------------------
"""

from functions import file_copy

# Call implemented file_copy function
file_copy(open("words.txt", "r"), open("new_words.txt", "w"))
