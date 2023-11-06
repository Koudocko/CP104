"""
-------------------------------------------------------
Displays statistics about a list
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-15"
-------------------------------------------------------
"""

# Imports
from functions import list_stats

values = [94, 96, -22, -79, -28, -26, -50, 71, 24, -32]

# Get key elements from list 
smallest, largest, total, average = list_stats(values)

# Display key elements of list
print(f"list_states({values})-> ({smallest}, {largest}, {total}, {average})")
