"""
-------------------------------------------------------
Counts the number of attributes in the text
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-15"
-------------------------------------------------------
"""

# Imports
from functions import comma_period_replace

# Get initial string
string = input("Input string with commas: ")

# Replace commas with periods in string
out = comma_period_replace(string)

# Display new replaced string
print(f"comma_period_replace({string}) -> ({out})")
