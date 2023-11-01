"""
-------------------------------------------------------
Displays information about calories burned on treadmill.
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-15"
-------------------------------------------------------
"""

# Imports
from functions import arrow_up

# Get number of rows in arrow
rows = int(input("Number of rows: "))

# Display up arrow
print(f"arrow_up({rows}) ->")
arrow_up(rows)
