"""
-------------------------------------------------------
Determines whether an employee qualifies for a loan
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-15"
-------------------------------------------------------
"""

# Imports
from functions import loan

# Get whether user is qualified for a loan
qualified = loan()

# Display qualification state
print(f"loan() -> {qualified}")
