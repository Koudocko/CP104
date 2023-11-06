"""
-------------------------------------------------------
Detects whether an input number is prime.
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-15"
-------------------------------------------------------
"""

# Imports
from functions import detect_prime

# Get number to be tested as prime
number = int(input("Input number: "))

# Display whether number is a prime number
prime = detect_prime(number)
print(f"detect_prime({number}) -> {prime}")

