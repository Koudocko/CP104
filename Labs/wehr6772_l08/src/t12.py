"""
-------------------------------------------------------
Sums the elements of two same-sized lists
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-15"
-------------------------------------------------------
"""

# Imports
from functions import list_sums

# Two lists to sum
source1 = [9, 9, 9]
source2 = [5.5, 2.7, 83]

# Sum two lists into one
target = list_sums(source1, source2)

print(f"list_sums({source1}, {source2}) -> {target}")
