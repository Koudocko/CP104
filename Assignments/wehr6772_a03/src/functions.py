"""
-------------------------------------------------------
Assignment 3 functions
-------------------------------------------------------
Author:  Tyler Wehrle
ID:      169056772
Email:   wehr6772@mylaurier.ca
__updated__ = "2023-09-15"
-------------------------------------------------------
"""

# Constants
SFEET_TO_ACRE = 43560 # Square feet to acre ratio
GRAVITY_ACCEL = 9.8 # Gravitational acceleration constant on Earth

def footage_to_acres(square_feet):
    """
    -------------------------------------------------------
    Converts square footage to acres.
    Use: acres = footage_to_acres(square_feet)
    -------------------------------------------------------
    Parameters:
        square_feet - area in square feet (float >= 0)
    Returns:
        acres - square_footage in acres (float)
    ------------------------------------------------------
    """

    # Compute acres using square feet and ratio
    acres = square_feet / SFEET_TO_ACRE
    return acres

def lawn_mow_time(width, length, speed):
    """
    -------------------------------------------------------
    Determines how long it takes to mow a rectangular lawn.
    Use: time = lawn_mow_time(width, length, speed)
    -------------------------------------------------------
    Parameters:
        width - width of a lawn in metres (float > 0)
        length - length of a lawn in metres (float > 0)
        speed - square metres cut per minute (float > 0)
    Returns:
        time_minutes - time required to mow the lawn (float)
    ------------------------------------------------------
    """

    # Compute time taken by dividing square meter lawn by speed
    time_minutes = (width * length) / speed
    return time_minutes

def extract_date(date_number):
    """
    -------------------------------------------------------
    Extracts the year, month, and day from a date number in the format YYYYMMDD.
    Use: year, month, day = extract_date(date_number)
    -------------------------------------------------------
    Parameters:
        date_number - a date number in the format YYYYMMDD (int)
    Returns:
        year - year portion of date_number (int)
        month - month portion of date_number (int)
        day - day portion of date_number (int)
    ------------------------------------------------------
    """

    # Compute the year with integer division
    year = date_number // 10000
    # Remove the year from the date_number
    remainder = date_number % 10000
    # Compute the month with integer division
    month = remainder // 100
    # Remove the month from the date, leftover is day
    day = remainder % 100

    return (year, month, day)

def multiply_fractions(num1, den1, num2, den2):
    """
    -------------------------------------------------------
    Calculates and returns fraction values.
    Use: num, den, product = multiply_fractions(num1, den1, num2, den2)
    -------------------------------------------------------
    Parameters:
        num1 - numerator of first fraction (int)
        den1 - denominator of first fraction (int != 0)
        num2 - numerator of second fraction (int)
        den2 - denominator of second fraction (int != 0)
    Returns:
        num - numerator of product (int)
        den - denominator of product (int)
        product - num / den (float)
    -------------------------------------------------------
    """

    # Compute numerator
    num = num1 * num2
    # Compute denominator
    den = den1 * den2 
    # Compute overall fraction product
    product = num / den

    return (num, den, product)

def falling_distance(falling_time):
    """
    -------------------------------------------------------
    Calculates distance an object has fallen due to gravity given
    the time it is fallen.
    Use: distance = falling_distance(falling_time)
    -------------------------------------------------------
    Parameters:
        falling_time - time object has fallen in seconds (int >= 0)
    Returns:
        distance - distance object has fallen in metres (float)
    -------------------------------------------------------
    """

    # Rearrange for time:
    # t = sqrt(2d/g)
    # t^2 = 2d/g
    # gt^2 = 2d
    # gt^2/2 = d

    # Compute distance object fell with respect to fall time
    distance = (falling_time ** 2) * GRAVITY_ACCEL / 2

    return distance
