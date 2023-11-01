"""
-------------------------------------------------------
Manage expenses and show details about budget status
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-15"
-------------------------------------------------------
"""

# Imports
from functions import employee_payroll

# Compute employee payroll based on user input
total, average = employee_payroll()

# Display total and average of payroll
print(f"({total:,.2f}, {average:,.2f})")
