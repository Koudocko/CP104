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
from functions import calories_treadmill

# Get calories per minute and number of minutes
per_min = float(input("Calories burned per minute: "))
minutes = int(input("Number of minutes on treadmill: "))

# Display calories information
print(f"calories_treadmill({per_min}, {minutes}) ->")
calories_treadmill(per_min, minutes)
