"""
-------------------------------------------------------
Draws a triange with a certain width and char type
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-15"
-------------------------------------------------------
"""

# Imports
from functions import draw_hollow_triangle

# Get width and symbol for triangle
width = int(input("Input width: "))
char = input("Input width: ")

# Draw triangle on screen
print(f"draw_hollow_triangle({width}, {char}) ->")
draw_hollow_triangle(width, char)
