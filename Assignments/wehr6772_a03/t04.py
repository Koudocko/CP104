"""
-------------------------------------------------------
Multiplies two fractions together
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-12"
-------------------------------------------------------
"""

from functions import multiply_fractions

# Get fraction components
num1 = int(input("Numerator 1: "))
den1 = int(input("Denominator 1: "))
num2 = int(input("Numerator 2: "))
den2 = int(input("Denominator 2: "))

# Get product of fractions
num, den, product = multiply_fractions(num1, den1, num2, den2)

# Display product of fractions
print(f"multiply_fractions({num1}, {den1}, {num2}, {den2}) -> {num}, {den}, {product}")
