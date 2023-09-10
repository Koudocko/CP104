"""
-------------------------------------------------------
Calculate money made from dog grooming for the day
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-09"
-------------------------------------------------------
"""

mortgage_principal = int(input("Mortgage principal ($): "))
num_months = int(input("Number of years: ")) * 12
monthly_interest = int(input("Yearly interest rate (%): ")) / 12

mortgage_numerator = monthly_interest * (1 + monthly_interest) ** num_months
mortgage_denominator = (1 + monthly_interest) ** num_months - 1
mortgage = mortgage_principal * mortgage_numerator / mortgage_denominator

print(f"The monthly payments are: $ {mortgage}")
