"""
-------------------------------------------------------
Displays the contents of a 2D matrix
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-09"
-------------------------------------------------------
"""

from functions import generate_matrix_num, print_matrix_num

# Call implemented print_matrix_num function
matrix = generate_matrix_num(3, 4, -10, 10, "float")
print_matrix_num(matrix, 'float')
