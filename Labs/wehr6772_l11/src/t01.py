"""
-------------------------------------------------------
Randomly generates a 2D matrix based on specifications
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-15"
-------------------------------------------------------
"""

# Imports
from functions import generate_matrix_num

# Get matrix specification
rows = int(input("Number of rows: "))
cols = int(input("Number of cols: "))
low = float(input("Low value of range: "))
high = float(input("High value of range: "))
value_type = input("Type of value: ")

# Get randomly generated matrix
matrix = generate_matrix_num(rows, cols, low, high, value_type)

# Display generated matrix
print(f'generate_matrix_num({rows}, {cols}, {low}, {high}, "{value_type}") -> {matrix}')
