"""
-------------------------------------------------------
Manage expenses and show details about budget status
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-09"
-------------------------------------------------------
"""

from functions import budget

# Call implemented budget function
expenses, balance, status = budget(200)
print(f"{expenses} {balance} {status}")

