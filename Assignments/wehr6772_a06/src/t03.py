"""
-------------------------------------------------------
Displays a table of monthly loan interest payments.
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-15"
-------------------------------------------------------
"""

# Imports
from functions import interest_table

# Get loan information
principal_amount = float(input("Principal amount: $"))
interest_rate = float(input("Interest rate (%): "))
payment = float(input("Payment amount: $"))

# Display whether number is a prime number
print(f"interest_data({principal_amount}, {interest_rate}, {payment}) ->")
interest_table(principal_amount, interest_rate, payment)
