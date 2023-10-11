"""
-------------------------------------------------------
Find the last longest word in words.txt
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-09"
-------------------------------------------------------
"""

from functions import find_longest

# Call implemented find_longest function
word = find_longest(open("words.txt", "r"))
