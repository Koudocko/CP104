"""
-------------------------------------------------------
Compute the total price of dosa from amount and price
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-12"
-------------------------------------------------------
"""

# Get dosa cost and amount
dosa_cost = float(input("Cost of 1 dosa: $"))
num_dosa = int(input("Number of dosa: "))

# Compute total from input variables
total = dosa_cost * num_dosa

print(f"Total cost of {num_dosa} dosa: ${total}")
