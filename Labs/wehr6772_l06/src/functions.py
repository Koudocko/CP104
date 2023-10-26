"""
-------------------------------------------------------
Lab 6 functions
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-15"
-------------------------------------------------------
"""

# Constants
# Number of weeks IAs work constant
NUM_WEEKS = 6

def sum_all(start, finish, increment):
    """
    -------------------------------------------------------
    Sums and returns all numbers from start to finish (inclusive)
    by increment.
    Use: total = sum_all(start, finish, increment)
    -------------------------------------------------------
    Parameters:
        start - an integer (int > 0)
        finish - an integer (int >= start)
        increment - an integer (int > 0)
    Returns:
        total - sum of all numbers from start to
            finish by increment (int)
    ------------------------------------------------------
    """

    # Use range in for loop to obtain nums to be summed 
    total = 0
    for num in range(start, finish + 1, increment):
        total += num

    return total

def draw_hollow_triangle(width, char):
    """
    -------------------------------------------------------
    Prints a hollow triangle of width characters using
    the char character.
    Use: draw_hollow_triangle(width, char)
    -------------------------------------------------------
    Parameters:
        width - number of characters wide (int > 0)
        char - the character to draw with (str, len() == 1)
    Returns:
        None
    ------------------------------------------------------
    """
    
    for num in range(0, width):
        if num == 0: # Top of triange edge case
            print(char)
        elif num == width - 1: # Every other row
            print(f"{'':{char}^{width}s}")
        else: # Bottom of triange edge case
            print(f"{char}{char:>{num}s}")

    return

def retirement(age, salary, increase):
    """
    -------------------------------------------------------
    Calculates a prints a table of how much a worker earns
    between age and retirement at 65.
    Use: retirement(age, salary, increase)
    -------------------------------------------------------
    Parameters:
        age - worker's current age (int > 0)
        salary - worker's current salary (float > 0)
        increase - percent increase in salary per year (float >= 0)
    Returns:
        None
    ------------------------------------------------------
    """


    # Display headers
    print("Age         Salary") 
    print("------------------")

    for year in range(age, 66):
        # Dynamic spacing size
        row_width = 18 - len(str(year))

        # Display the row values of age and salary
        print(f"{year}{salary:>{row_width},.2f}")
        # Increase salary
        salary *= 1 + (increase / 100)
    
    return

def lumber(b_min, b_max, b_inc, h_min, h_max, h_inc):
    """
    -------------------------------------------------------
    Create a table of the engineering properties of lumber.
    Given the base and height of a piece of lumber in inches,
    different properties of a piece of lumber are calculated as:
        cross-sectional area = base × height
        moment of inertia = base × height^3 / 12
        section modulus = base × height^2 / 6
    Use: lumber(b_min, b_max, b_inc, h_min, h_max, h_inc)
    -------------------------------------------------------
    Parameters:
        b_min - minimum value of base (int > 0)
        b_max - maximum value of base (int > b_min)
        b_inc - increment in base value (int > 0)
        h_min - minimum value of height (int > 0)
        h_max - maximum value of height (int > h_min)
        h_inc - increment in height value (int > 0)
    Returns:
        None
    -------------------------------------------------------
    """

    # Display headers
    print("              Cross-Sectional  Moment of  Section")
    print("Base  Height  Area             Inertia    Modulus")
    print("-------------------------------------------------")

    # Nested for loops, heights as the inner and bases as the outer
    for base in range(b_min, b_max + 1, b_inc):
        for height in range(h_min, h_max + 1, h_inc):
            # Compute properties of lumber
            cross_sectional_area = base * height
            moment_of_inertia = base * height ** 3 / 12
            section_modulus = base * height ** 2 / 6

            # Display row with lumber properties data
            print(f"{base:>4d}  X{height:>5d} {cross_sectional_area:>16.2f} {moment_of_inertia:>10.2f} {section_modulus:>8.2f}")

    return

def ia_hours(ia_count):
    """
    -------------------------------------------------------
    Calculates the total number of hours that IAs (Instructional
    Assistants) work over a 6 week period by asking for the hours
    for each IA per week.
    Use: total_hours = ia_hours(ia_count)
    -------------------------------------------------------
    Parameters:
        ia_count - number of IAs (int > 0)
    Returns:
        total_hours - hours worked by all IAs (float)
    ------------------------------------------------------
    """

    
    # Iterate from 1 to NUM_WEEKS (inclusive)
    total_hours = 0
    for week in range(1, NUM_WEEKS + 1):
        print(f"Week {week}")

        # Iterate over input for each IA in the week
        for ia in range(1, ia_count + 1):
            hours = float(input(f"  Marking hours for IA {ia}: "))
            total_hours += hours
    
    return total_hours
