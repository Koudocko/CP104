"""
-------------------------------------------------------
Calculates the balance growth via compound interest over time
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-12"
-------------------------------------------------------
"""

# Get input variables
principal = float(input("Principal: $"))
interest = float(input("Interest (%): "))
num_years = int(input("Number of years: "))
num_compound = int(input("Number of times interest compounded per year: "))

# Convert interest from percent to decimal
interest /= 100
# Use compound interest formula with input variables
balance = principal * (1 + (interest / num_compound)) ** (num_compound * num_years)

# Display the user's final balance
print(f"Balance: $ {balance}")
