"""
-------------------------------------------------------
Divide flyers amonst the number of delivery people
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-12"
-------------------------------------------------------
"""

# Get number of flyers and delivery people
num_flyers = int(input("Number of flyers: "))
num_people = int(input("Number of delivery people: "))

# Compute flyers per delivery person
flyers_per = num_flyers // num_people
# Computer flyers left over
flyers_left = num_flyers % num_people

# Display flyers per person and flyers left
print(f"Flyers per delivery person: {flyers_per}")
print(f"Flyers left over: {flyers_left}")
