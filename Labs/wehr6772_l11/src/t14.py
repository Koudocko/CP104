"""
-------------------------------------------------------
Swap the rows and columns of a 2D matrix
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-15"
-------------------------------------------------------
"""

# Imports
from functions import matrix_transpose, generate_matrix_num

# Get matrix specification
rows = int(input("Number of rows: "))
cols = int(input("Number of cols: "))
low = float(input("Low value of range: "))
high = float(input("High value of range: "))

# Get randomly generated matrix
matrix = generate_matrix_num(rows, cols, low, high, "int")

# Transpose the matrix
transposed = matrix_transpose(matrix)

# Display transposed matrix
print(f"matrix_transpose({matrix}) -> {transposed}")
