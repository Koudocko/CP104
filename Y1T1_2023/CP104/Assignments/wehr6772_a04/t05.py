"""
-------------------------------------------------------
Outputs a quirky phrase based on the number input.
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-12"
-------------------------------------------------------
"""

# Imports
from functions import hoo_rah

# Get number to be used
number = int(input("Number: "))

# Obtain quirky phrase output
output = hoo_rah(number)

# Display quirky phrase
print(f"hoo_rah({number}) -> {output}")
