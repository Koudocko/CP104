"""
-------------------------------------------------------
Computes discount price given inital and percentage discount
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-09"
-------------------------------------------------------
"""

# Obtain inital number and percentage discount
number = float(input("Enter number: "))
percent = float(input("Enter percent: ")) 

# Compute the discount by amount
discount = number * percent / 100

print(f"A {percent} percent discount on {number} is {discount:.1f}")
