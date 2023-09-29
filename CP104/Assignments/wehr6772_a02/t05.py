"""
-------------------------------------------------------
Compute amount and cost of resources needed for a building
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-12"
-------------------------------------------------------
"""

# Get building specifications
foundation_length = float(input("Foundation length (m): "))
foundation_width = float(input("Foundation width (m): "))
foundation_height = float(input("Foundation height (m): "))
wall_height = float(input("Well height (m): "))
concrete_rate = float(input("Cost of concrete ($/m^3): "))
brick_rate = float(input("Cost of bricks ($/m^2): "))

# Compute concrete needed from foundation dimensions
concrete_needed = foundation_length * foundation_width * foundation_height
# Compute cost using the rate and m^3 needed
concrete_cost = concrete_rate * concrete_needed

# Compute brick needed from wall dimensions
brick_needed = 2 * wall_height * (foundation_width + foundation_length)
# Compute brick cost using the rate and m^2 needed
brick_cost = brick_rate * brick_needed

# Sum the two costs for the total
total_cost = concrete_cost + brick_cost

# Display computed statistics
print(f"Concrete needed for foundation (m^3): {concrete_needed}")
print(f"Cost of concrete: ${concrete_cost:,.2f}")
print(f"Bricks needed for walls (m^2): {brick_needed}")
print(f"Cost of bricks: ${brick_cost:,.2f}")
print(f"Total cost: ${total_cost:,.2f}")
