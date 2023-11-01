"""
-------------------------------------------------------
Randomly generated guessing game
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-15"
-------------------------------------------------------
"""

# Imports
from functions import hi_lo_game

# Get random value ceiling
high = int(input("Enter maximum random value (>1): "))

# Play high low game and get guess count
count = hi_lo_game(high)

# Display number of guesses taken
print(f"You made {count} guesses.")
