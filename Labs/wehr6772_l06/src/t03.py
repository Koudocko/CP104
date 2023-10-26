"""
-------------------------------------------------------
Sums all numbers in range with respect to increment
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-15"
-------------------------------------------------------
"""

# Imports
from functions import sum_all

# Get range and increment value
start = int(input("Input start: "))
finish = int(input("Input finish: "))
increment = int(input("Input increment: "))

# Compute sum of numbers within range
total = sum_all(start, finish, increment)

# Display the sum of numbers
print(f"sum_all({start}, {finish}, {increment}) -> {total}")
