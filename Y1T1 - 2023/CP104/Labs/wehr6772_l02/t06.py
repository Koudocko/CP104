"""
-------------------------------------------------------
Calculate mortgage monthly payments
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-09"
-------------------------------------------------------
"""

# Collect input values
mortgage_principal = float(input("Mortgage principal ($): "))
num_months = int(input("Number of years: "))
num_months *= 12
monthly_interest = float(input("Yearly interest rate (%): "))
monthly_interest = monthly_interest / 100 / 12

# Compute equation numerator
mortgage_numerator = monthly_interest * (1 + monthly_interest) ** num_months
# Compute equation denominator
mortgage_denominator = (1 + monthly_interest) ** num_months - 1
# Compute entire equation
mortgage = mortgage_principal * mortgage_numerator / mortgage_denominator

print(f"The monthly payments are: $ {mortgage}")
