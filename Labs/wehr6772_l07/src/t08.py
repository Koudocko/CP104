"""
-------------------------------------------------------
Manage expenses and show details about budget status
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-15"
-------------------------------------------------------
"""

# Imports
from functions import budget

# Get the initial available balance
available = float(input("Enter available balance: "))

# Compute budget stats based on initial balance
expenses, balance, status = budget(available)

# Display budget stats
print(f"({expenses}, {balance}, '{status}')")
