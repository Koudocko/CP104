# Constants
# Minimum number of employement years to be eligible for a loan
MIN_EMPLOYMENT_TIME = 5
# Minimum salary to be eligible for a loan
MIN_SALARY = 30000

def magic_date(day, month, year):
    """
    -------------------------------------------------------
    Determines if a date is magic. A date is magic if the day
    times the month equals the year.
    Use: magic = magic_date(day, month, year)
    -------------------------------------------------------
    Parameters:
        day - numeric day (int > 0)
        month - numeric month (int > 0)
        year - numeric two-digit year (int > 0)
    Returns:
        magic - True if date is magic, False otherwise (boolean)
    -------------------------------------------------------
    """

    # Set magic to True date if day times month equals year, else False
    if day * month == year:
        magic = True
    else:
        magic = False

    return magic

def is_divisible(n, i, j):
    """
    -------------------------------------------------------
    Determines if n is evenly divisible by both i and j.
    Use: result = is_divisible(n, i, j)
    -------------------------------------------------------
    Parameters:
        n - the number to check for divisibility (int)
        i - one of the values to divide n by (int)
        j - another value to divide n by (int)
    Returns:
        result - True if n is evenly divisible by both
            i and j, False otherwise (boolean)
    ------------------------------------------------------
    """

    if n % i == 0 and n % j == 0:
        result = True
    else:
        result = False

    return result

def wind_speed(speed):
    """
    -------------------------------------------------------
    description
    Use: category = wind_speed(speed)
    -------------------------------------------------------
    Parameters:
        speed - wind speed in km/hr (int >= 0)
    Returns:
        category - description of wind speed (str)
    ------------------------------------------------------
    """

    # Fallthrough algorithm to determine category
    if speed >= 118:
        category = "Hurricane"
    elif speed >= 89:
        category = "Whole Gale"
    elif speed >= 62:
        category = "Gale Winds"
    elif speed >= 39:
        category = "Strong Wind"
    elif speed >= 0:
        category = "Breeze"
    else:
        category = "Unknown"

    return category

def quadrant(x, y):
    """
    -------------------------------------------------------
    Determines location on a plane of an x, y coordinate.
    Use: location = quadrant(x, y)
    -------------------------------------------------------
    Parameters:
        x - x coordinate on a Cartesian plane (float)
        y - y coordinate on a Cartesian plane (float)
    Returns:
        location - one of: 'Quadrant 1', 'Quadrant 2', 'Quadrant 3'
          'Quadrant 4', 'X-Axis', 'Y-Axis', 'Origin' (str)
    -------------------------------------------------------
    """

    # Defaults to X-Axis to cover overlap
    location = "X-Axis"

    # Cover all combinations of x/y coordinates
    if x > 0:
        if y > 0:
            location = "Quadrant 1"
        elif y < 0:
            location = "Quadrant 4"
    elif x < 0:
        if y > 0:
            location = "Quadrant 2"
        elif y < 0:
            location = "Quadrant 3"
    else:
        if y == 0:
            location = "Origin"
        else:
            location = "Y-Axis"

    return location

def loan():
    """
    -------------------------------------------------------
    An employee may qualify for a loan if they have worked for a
    minimum of 5 years, and has a salary of $30,000 or more.
    This function must ask for the years employed and the salary
    as appropriate.
    Use: qualified = loan()
    -------------------------------------------------------
    Returns:
        qualified - True if employee qualifies for a loan,
            False otherwise (boolean)
    -------------------------------------------------------
    """


    # Obtain years employed
    years_employed = int(input("Years employed: "))

    # Nested if statements to prevent empty annual salary from failing
    if years_employed >= MIN_EMPLOYMENT_TIME:
        # Obtain annual salary
        annual_salary = int(input("Annual salary: "))

        if annual_salary >= MIN_SALARY:
            qualified = True
        else:
            qualified = False
    else:
        qualified = False

    return qualified
