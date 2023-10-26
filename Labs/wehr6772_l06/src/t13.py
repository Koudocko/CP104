"""
-------------------------------------------------------
Display a chart of lumber properties based on height/base ranges
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-15"
-------------------------------------------------------
"""

# Imports
from functions import lumber

# Get lumber properties
b_min = int(input("Input base minimum: "))
b_max = int(input("Input base maximum: "))
b_inc = int(input("Input base increment: "))
h_min = int(input("Input height minimum: "))
h_max = int(input("Input height maximum: "))
h_inc = int(input("Input height increment: "))

# Display table of lumber properties
print(f"lumber({b_min}, {b_max}, {b_inc}, {h_min}, {h_max}, {h_inc}) ->")
lumber(b_min, b_max, b_inc, h_min, h_max, h_inc)
