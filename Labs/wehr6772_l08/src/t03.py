"""
-------------------------------------------------------
Displays the name of a given digit
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-15"
-------------------------------------------------------
"""

# Imports
from functions import get_digit_name

# Get digit
n = int(input("Enter digit (0 <= n <= 9): "))

# Get name of the digit
name = get_digit_name(n)

# Display name of the digit
print(f"'{name}'")
