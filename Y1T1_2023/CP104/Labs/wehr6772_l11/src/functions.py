from random import randint, uniform

def generate_matrix_num(rows, cols, low, high, value_type):
    """
    -------------------------------------------------------
    Generates a 2D list of numbers of the given type, 'float' or 'int'.
    (To generate random float number use random.uniform and to
    generate random integer number use random.randint)
    Use: matrix = generate_matrix_num(rows, cols, low, high, value_type)
    -------------------------------------------------------
    Parameters:
        rows - number of rows in the list (int > 0)
        cols - number of columns (int > 0)
        low - low value of range (float)
        high - high value of range (float > low)
        value_type - type of values in the list, 'float' or 'int' (str)
    Returns:
        matrix - a 2D list of random numbers (2D list of float/int)
    -------------------------------------------------------
    """

    # Initialize empty matrix
    matrix = []

    if value_type == "int":
        for _ in range(0, rows):
            row = []

            # Create random row
            for _ in range(0, cols):
                # If value type is int use randint
                row.append(randint(low, high))

            # Push random row
            matrix.append(row)
    elif value_type == "float":
        for _ in range(0, rows):
            row = []

            for _ in range(0, cols):
                # If value type is float use uniform
                row.append(uniform(low, high))

            matrix.append(row)

    return matrix


def print_matrix_num(matrix, value_type):
    """
    -------------------------------------------------------
    Prints the contents of a 2D list in a formatted table.
    Prints float values with 2 decimal points and prints row and
    column headings.
    Use: print_matrix_num(matrix, 'float')
    Use: print_matrix_num(matrix, 'int')
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of values (2D list)
        value_type - type of values in the list, 'float' or 'int' (str)
    Returns:
        None.
    -------------------------------------------------------
    """

    # Number of columns constant
    NUM_COLS = len(matrix[0])

    # Dynamic formatter based on value_type
    if value_type == "float":
        fmt = '.2f'
    else: 
        fmt = 'd'

    # Print the column header
    print(" ", end="")
    for col in range(0, NUM_COLS):
        print(f"{col:>7d}", end="")
    print('\n')

    # Iterate over rows of the 2D matrix
    for idx, row in enumerate(matrix):
        print(f"{idx}", end="") 

        # Iterate over cols of the 2D matrix
        for col in row:
            print(f"{col:>7{fmt}}", end="")
        print('\n')

    return

def find_position(matrix):
    """
    -------------------------------------------------------
    Determines the first locations [row, column] of smallest and
    largest values in a 2D list.
    Use: s_loc, l_loc = find_position(matrix)
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of numbers (2D list)
    Returns:
        s_loc - a list of of the row and column location of
            the smallest value in matrix (list of int)
        l_loc - a list of of the row and column location of
            the largest value in matrix (list of int)
    -------------------------------------------------------
    """

    # Default max and min values
    min = matrix[0][0]
    max = min

    # Default max and min coordinates
    s_loc = [0, 0]
    l_loc = [0, 0]

    # Iterate over full matrix, update above variables based on comparisons
    for idx_r, row in enumerate(matrix):
        for idx_c, col in enumerate(row):
            if col < min:
                min = col
                s_loc = [idx_r, idx_c]
            if col > max:
                max = col
                l_loc = [idx_r, idx_c]

    return (s_loc, l_loc)

def matrix_scalar_multiply(matrix, num):
    """
    -------------------------------------------------------
    Update matrix by multiplying each element of matrix by num.
    Use: matrix_scalar_multiply(matrix, num)
    -------------------------------------------------------
    Parameters:
        matrix - the matrix to multiply (2D list of int/float)
        num - the number to multiply by (int/float)
    Returns:
        None
    ------------------------------------------------------
    """

    # Iterate over every element in matrix and multiply by num
    for row in range(0, len(matrix)):
        for col in range(0, len(matrix[row])):
            matrix[row][col] *= num

    return

def matrix_transpose(matrix):
    """
    -------------------------------------------------------
    Transpose the contents of matrix. (Swap the rows and columns.)
    Use: transposed = matrix_transpose(matrix):
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list (2D list of *)
    Returns:
        transposed - the transposed matrix (2D list of *)
    ------------------------------------------------------
    """

    # Initialze new transposed list
    transposed = []
    
    # Process the same column of each row before moving on
    for col in range(0, len(matrix[0])):
        new_row = []

        for row in range(0, len(matrix)):
            new_row.append(matrix[row][col]) 
        transposed.append(new_row)

    return transposed
