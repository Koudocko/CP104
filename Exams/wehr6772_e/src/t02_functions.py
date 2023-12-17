"""
-------------------------------------------------------
Exam Task 2 Function Definitions
-------------------------------------------------------
Author: Tyler Wehrle
ID:     169056772
Email:  wehr6772@mylaurier.ca
__updated__ = "2023-08-25"
-------------------------------------------------------
"""
# Constants

# Your constants here
WET_MM = 8
DAMP_MM = 4
DRY_MM = 0
STOP_VAL = -1


def rainfall():
    """
    -------------------------------------------------------
    Asks the user for daily rainfall (in mm) from the keyboard.
    The function stops asking for rainfall when the user enters -1.
    The function returns:
        the total number of dry days (rainfall lower than 4mm)
        the total number of damp days (rainfall 4mm - 8mm)
        the total number of wet days (rainfall greater than 8mm)
        the average rainfall for all days (rounded down)
    Do all inputs and calculations in integer.
    Use: dry_days, damp_days, wet_days, avg = rainfall()
    -------------------------------------------------------
    Returns‌​‌​​​​‌​​‌‌‌​​‌‌​‌​​​​​​‌​​:
        dry_days - number of dry days (int)
        damp_days - number of damp days (int)
        wet_days - number of wet days (int)
        avg - average rainfall of all days (int)
    -------------------------------------------------------
    """

    # your code here
    dry_days, damp_days, wet_days, total = 0, 0, 0, 0
    mm = int(input("Rainfall mm (-1 to stop): "))

    while mm != STOP_VAL:
        if mm > WET_MM:
            wet_days += 1
        elif mm >= DAMP_MM:
            damp_days += 1
        elif mm >= DRY_MM:
            dry_days += 1

        total += mm
        mm = int(input("Rainfall mm (-1 to stop): "))

    return (dry_days, damp_days, wet_days, total // (dry_days + damp_days + wet_days))
