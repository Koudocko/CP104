"""
-------------------------------------------------------
Multiplies every element in matrix by a number
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-15"
-------------------------------------------------------
"""

# Imports
from functions import matrix_scalar_multiply, generate_matrix_num
from copy import deepcopy

# Get matrix specification
rows = int(input("Number of rows: "))
cols = int(input("Number of cols: "))
low = float(input("Low value of range: "))
high = float(input("High value of range: "))
value_type = input("Type of value: ")

# Get multiplier
num = float(input("Scalar multilier: "))

# Get randomly generated matrix
matrix = generate_matrix_num(rows, cols, low, high, value_type)
copy_matrix = deepcopy(matrix)

# Updates matrix with muliplier
matrix_scalar_multiply(matrix, num)

# Display updated matrix
print(f"matrix_scalar_multiply({copy_matrix}, {num}) -> {matrix}")
