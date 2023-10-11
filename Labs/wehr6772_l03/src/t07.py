"""
-------------------------------------------------------
Computes the total cost of all three meals in the day
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-09"
-------------------------------------------------------
"""

# Obtain meal costs
breakfast_cost = float(input("Enter cost of breakfast: $"))
lunch_cost = float(input("Enter cost of lunch: $"))
supper_cost = float(input("Enter cost of supper: $"))

# Compute total cost
total_cost = breakfast_cost + lunch_cost + supper_cost

# Format the costs as a bill
print(f"Meal         Cost")
print(f"Breakfast    ${breakfast_cost:6.2f}")
print(f"Lunch        ${lunch_cost:6.2f}")
print(f"Supper       ${supper_cost:6.2f}")
print(f"Total        ${total_cost:6.2f}")
