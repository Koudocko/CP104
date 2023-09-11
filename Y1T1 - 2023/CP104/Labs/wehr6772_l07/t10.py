"""
-------------------------------------------------------
Manage expenses and show details about budget status
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-09"
-------------------------------------------------------
"""

from functions import employee_payroll

# Call implemented employee_payroll function
total, average = employee_payroll()
print(f"{total} {average}")
