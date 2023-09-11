"""
-------------------------------------------------------
Display information about a set of numbers from numbers.txt
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-09"
-------------------------------------------------------
"""

from functions import number_stats

# Call implemented number_stats function
smallest, largest, total, average = number_stats(open("numbers.txt", "r"))
