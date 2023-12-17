"""
-------------------------------------------------------
Exam Task 5 Function Definitions
-------------------------------------------------------
Author: Tyler Wehrle
ID:     169056772
Email:  wehr6772@mylaurier.ca
__updated__ = "2023-12-13"
-------------------------------------------------------
"""


def fill_matrix(fh_in, rows, cols):
    """
    -------------------------------------------------------
    Creates a rows by cols 2D list of integers filled with
    space-separated integers from f_in. If f_in does not have enough values,
    fill the remaining slots with 0s. If f_in has too many values,
    the excess values are ignored.
    Use: matrix = fill_matrix(fh_in, rows, cols)
    -------------------------------------------------------
    Parameters:
        fh_in - the integers file to process (file handle - already open for reading)
        rows - rows in matrix (int > 0)
        cols - columns in matrix (int > 0)
    Returns‌​‌​​​​‌​​‌‌‌​​‌‌​‌​​​​​​‌​​:
        matrix - a 2D list of integers (2D list of int)
    -------------------------------------------------------
    """

    # Your code here
    line = " "
    matrix = [[0 for _ in range(cols)] for _ in range(rows)]

    row_offset, col_offset = 0, 0

    while line != "" and row_offset < len(matrix):
        line = fh_in.readline()

        for val in line.split():
            matrix[row_offset][col_offset] = val
            col_offset += 1

            if col_offset >= cols:
                row_offset += 1
                col_offset = 0

            if row_offset >= rows:
                break

    return matrix
