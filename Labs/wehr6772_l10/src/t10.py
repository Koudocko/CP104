"""
-------------------------------------------------------
Fetches the frequency of a word occuring in words.txt
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-09"
-------------------------------------------------------
"""

from functions import count_frequency_word

# Call implemented count_frequency_word function
count = count_frequency_word(open("words.txt", "r"), "Exercise")
