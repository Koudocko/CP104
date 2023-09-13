"""
-------------------------------------------------------
Retrieves the longest common ending between two stings.
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-12"
-------------------------------------------------------
"""

# Imports
from functions import common_end

# Get two strings
str1 = input("Input string 1: ")
str2 = input("Input string 2: ")

# Get longest common ending 
suffix = common_end(str1, str2)

# Print longest commong ending
print(f"common_end('{str1}', '{str2}') -> {suffix}")
