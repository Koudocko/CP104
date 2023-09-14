"""
-------------------------------------------------------
Computes the total pay for the week
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-09"
-------------------------------------------------------
"""

# Obtain hourly rate and hours worked for the week
hourly_rate = float(input("Hourly rate of pay: $"))
hours_worked = float(input("Hours worked in the week: "))

# Calculate total pay for the week
total_pay = hourly_rate * hours_worked

# Display total pay for the week
print(f"Total pay for the week: ${total_pay:.2f}")
