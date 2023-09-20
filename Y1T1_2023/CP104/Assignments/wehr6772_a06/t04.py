"""
-------------------------------------------------------
Displays the number of digits in a number.
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-12"
-------------------------------------------------------
"""

# Imports
from functions import count_of_digits

# Get input number
number = int(input("Input number: "))

# Compute number of digits in number
digits = count_of_digits(number)

# Display number of digits in number
print(f"count_of_digits({digits}) -> {digits}")
