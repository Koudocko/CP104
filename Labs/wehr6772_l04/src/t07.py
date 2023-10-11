"""
-------------------------------------------------------
Computes the total value of change from sets of coins
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-15"
-------------------------------------------------------
"""

# Imports
from functions import total_change

# Get number of each type of coin
nickels = int(input("Number of nickels: "))
dimes = int(input("Number of dimes: "))
quarters = int(input("Number of quarters: "))
loonies = int(input("Number of loonies: "))
toonies = int(input("Number of toonies: "))

# Compute the total change from the coin quanitites
total = total_change(nickels, dimes, quarters, loonies, toonies)

# Display total change
print(f"total_change({nickels}, {dimes}, {quarters}, {loonies}, {toonies}) -> {total}")
