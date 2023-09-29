"""
-------------------------------------------------------
Computes amount of each ingredient needed for some servings
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-15"
-------------------------------------------------------
"""

# Constants
# Per 6 serving of Mac & Cheese
MILK = 4 # Cups
BUTTER = 8 # Tablespoons
FLOUR = 0.5 # Cups
SALT = 2 # Tablespoons

# Obtain number of servings
num_servings = int(input("Enter servings of Mac & Cheese: "))

# Normalize amounts to per num_servings
servings_ratio = num_servings / 6 

# Compute amounts per ingredient
milk_amount = servings_ratio * MILK
butter_amount = servings_ratio * BUTTER
flour_amount = servings_ratio * FLOUR
salt_amount = servings_ratio * SALT

# Display amounts needed per ingredient
print(f"{num_servings} servings of Mac & Cheese requires:")
print(f"milk (cups): {milk_amount:.2f}")
print(f"butter (cups): {butter_amount:.2f}")
print(f"flour (cups): {flour_amount:.2f}")
print(f"salt (cups): {salt_amount:.2f}")
