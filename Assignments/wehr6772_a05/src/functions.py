"""
-------------------------------------------------------
Assignment 5 functions
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-15"
-------------------------------------------------------
"""

# Constants
CALORIE_INTERVAL = 5
ARROW_CHAR = '#'

def calc_factorial(number):
    """
    -------------------------------------------------------
    Calculates and returns the factorial of number.
    Use: product = calc_factorial(number)
    -------------------------------------------------------
    Parameters:
        number - number to factorial (int > 0)
    Returns:
        product - number! (int)
    ------------------------------------------------------
    """

    # Initialize product to start at 1
    product = 1
    # Multiply product with range [1, number]
    for num in range(1, number + 1):
        product *= num

    return product

def calories_treadmill(per_min, minutes):
    """
    -------------------------------------------------------
    Prints a table of the number of calories burned,
    from using the treadmill at each interval.
    Use: calories_treadmill(per_min, minutes)
    -------------------------------------------------------
    Parameters:
        per_min - number of calories burned per minute (int > 0) 
        minutes - number of minutes on the treadmill (int > 0)
    Returns:
        None
    ------------------------------------------------------
    """

    # Starting calories
    calories_burned = 0
    # Start at the interval, end at minutes (inclusive), increment by interval
    for time in range(CALORIE_INTERVAL, minutes + 1, CALORIE_INTERVAL):
        # Compute number of calories burned
        calories_burned = time * per_min

        # Display number of calories burned at interval
        print(f"{time:3d}{calories_burned:6.1f}") 

    return

def arrow_up(rows):
    """
    -------------------------------------------------------
    Display an upwards facing arrow based on a height.
    Use: arrow_up(rows)
    -------------------------------------------------------
    Parameters:
        rows - number of rows in up arrow (int >= 0)
    Returns:
        None
    ------------------------------------------------------
    """

    # Generate number of rows
    for row in range(0, rows):
        # Edge case for start
        if row == 0:
            print(f"{ARROW_CHAR:>{rows}s}")
        else:
            # Left character offset
            l_offset = rows - row
            # Right character offset
            r_offset = (row * 2)

            # Display left and right characters
            print(f"{ARROW_CHAR:>{l_offset}s}", end="")
            print(f"{ARROW_CHAR:>{r_offset}s}")

    return

def multiplication_table(start_num, stop_num):
    """
    -------------------------------------------------------
    Prints a multiplication table for values from start_num to stop_num.
    Use: multiplication_table(start_num, stop_num)
    -------------------------------------------------------
    Parameters:
        start_num - the range start value (int)
        stop_num - the range stop value (int)
    Returns:
        None
    ------------------------------------------------------
    """

    # Allows for bi-directional multiplication table
    if start_num < stop_num:
        increment = 1
    else:
        increment = -1

    # Print header
    print(f"{'':>7s}", end="")
    for row in range(start_num, stop_num + increment, increment):
        print(f"{row:5d}", end="")
    print('')

    # Print horizontal line
    bar_length = 5 * (abs(start_num - stop_num) + 1)
    print(f"{'':>7s}{'':->{bar_length}s}")

    # Includes [start_num, stop_num]
    for row in range(start_num, stop_num + increment, increment):
        # Print row label
        print(f"{row:5d} |", end="")

        # Display each column in row
        for col in range(start_num, stop_num + increment, increment):
            # Compute product between row and column
            result = row * col

            print(f"{result:5d}", end="")

        print('')

    return

def range_addition(start, increment, count):
    """
    -------------------------------------------------------
    Uses a for loop to sum values from start by increment.
    Use: total = range_addition(start, increment, count)
    -------------------------------------------------------
    Parameters:
        start - the range start value (int)
        increment - the range increment (int)
        count - the number of values in the range (int)
    Returns:
        total - the sum of the range (int)
    ------------------------------------------------------
    """

    # Initialize total
    total = 0

    # Get end based on start and increment
    end = start + (increment * (count - 1)) + (1 * (increment // abs(increment)))

    # Range specifications:
    # Start - start
    # End - start + (count (excluding the start) * interval increase amount
    # Increment - increment
    for num in range(start, end, increment):
        # Add interval in range to total
        total += num

    return total
